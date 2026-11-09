#!/usr/bin/env bash
# Builds and serves the wiki locally. Open http://localhost:4000/wiki/home when it is ready.
#   ./wiki.sh build   reuses the previous build      ./wiki.sh clean   full rebuild
#   add "all" to also build the translations

# The script lives in tools; the wiki is one folder up.
cd "$(dirname "${BASH_SOURCE[0]}")/.." || exit 1

# Start of the timer for the "Total time" line printed after the build.
T_START=$(date +%s)

JEKYLL_PORT=4000
# 127.0.0.1 is reachable from this computer only. Run with JEKYLL_HOST=0.0.0.0
# to let other devices on the network open it.
JEKYLL_HOST="${JEKYLL_HOST:-127.0.0.1}"
JEKYLL_BASEURL=/wiki

# "build" is the default, "clean" forces a full rebuild, "all" also builds the translations.
JEKYLL_CONFIG=_config.yml,_config.local.yml,_config.local.en.yml
JEKYLL_CLEAN=0
for arg in "$@"; do
    # Accepts build, clean, all, buildAll and cleanAll, with or without leading dashes.
    opt=$(printf '%s' "$arg" | tr 'A-Z' 'a-z' | tr -d '-')
    case "$opt" in
        build) ;;
        clean) JEKYLL_CLEAN=1 ;;
        all|buildall) JEKYLL_CONFIG=_config.yml,_config.local.yml ;;
        cleanall) JEKYLL_CLEAN=1; JEKYLL_CONFIG=_config.yml,_config.local.yml ;;
        *) echo "Unknown option \"$arg\". Use: ./wiki.sh build, ./wiki.sh clean, ./wiki.sh build all, ./wiki.sh clean all"; exit 1 ;;
    esac
done

# Walk up to the site root, so Jekyll is never started from the wrong folder.
depth=0
while [ ! -f "_config.yml" ]; do
    depth=$((depth + 1))
    if [ "$depth" -ge 10 ] || [ "$PWD" = "/" ]; then
        echo "Could not find _config.yml - put this script in or below the wiki folder."
        exit 1
    fi
    cd ..
done

echo "Site root: $PWD"
echo

# Jekyll 3 only loads the github-pages plugins (theme, markdown) when a file
# named Gemfile is in the site root, so copy it there. It is git-ignored.
[ -f Gemfile ] || cp .env-files/Gemfile.github Gemfile
export BUNDLE_GEMFILE="$PWD/Gemfile"

# "clean" throws away the previous build and the cached theme, to force a full rebuild.
if [ "$JEKYLL_CLEAN" = "1" ]; then
    rm -rf _site .jekyll-metadata .theme-cache
fi

for tool in git ruby bundle; do
    command -v "$tool" || echo "$tool: not found"
done
if ! command -v bundle >/dev/null 2>&1; then
    echo
    echo "Bundler was not found. Install Ruby (https://jekyllrb.com/docs/installation/) and run: gem install bundler"
    exit 1
fi
echo

if ! bundle check >/dev/null 2>&1; then
    echo "Installing gems..."
    bundle install || { echo; echo "bundle install failed - see the messages above."; exit 1; }
    echo
fi

# Stop an old server still holding the port, or it keeps serving the old build.
old_pids=""
if command -v lsof >/dev/null 2>&1; then
    old_pids=$(lsof -ti "tcp:$JEKYLL_PORT" -sTCP:LISTEN 2>/dev/null)
elif command -v fuser >/dev/null 2>&1; then
    old_pids=$(fuser "$JEKYLL_PORT/tcp" 2>/dev/null)
fi
if [ -n "$old_pids" ]; then
    for pid in $old_pids; do
        echo "Stopping old server (PID $pid)..."
        kill "$pid" 2>/dev/null
    done
    sleep 1
fi

echo "Open http://localhost:$JEKYLL_PORT$JEKYLL_BASEURL/home when the server is ready. Press Ctrl+C to stop it."
echo

# Build first, so the total time can be printed, then serve what was built.
# Keeps the theme in .theme-cache so unchanged pages are skipped on the next run.
export RUBYOPT="-r./tools/local_theme_cache.rb"
bundle exec jekyll build --baseurl "$JEKYLL_BASEURL" --config "$JEKYLL_CONFIG" --incremental --verbose \
    || { echo; echo "The build failed - see the messages above."; exit 1; }

T_TOTAL=$(( $(date +%s) - T_START ))
echo
echo "Total time from start to finished build: $((T_TOTAL / 60)) min $((T_TOTAL % 60)) s ($T_TOTAL seconds)"
echo "Options used: ${*:-build - English only, reusing the previous build}"
echo "Open http://localhost:$JEKYLL_PORT$JEKYLL_BASEURL/home - press Ctrl+C to stop the server."
echo

exec bundle exec jekyll serve --skip-initial-build --host "$JEKYLL_HOST" --port "$JEKYLL_PORT" --baseurl "$JEKYLL_BASEURL" --config "$JEKYLL_CONFIG" --incremental --verbose
