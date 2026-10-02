@echo off
rem Serves the wiki locally. Open http://localhost:4000/wiki/home when it is ready.

cd /d "%~dp0"

rem Start of the timer for the "Total time" line printed after the build.
for /f %%T in ('ruby -e "print Time.now.to_i" 2^>nul') do set T_START=%%T

set JEKYLL_PORT=4000
rem 127.0.0.1 is reachable from this computer only. Set JEKYLL_HOST=0.0.0.0
rem before running to let other devices on the network open it.
if not defined JEKYLL_HOST set JEKYLL_HOST=127.0.0.1
set JEKYLL_BASEURL=/wiki

rem Options: "all" also builds the translations, "clean" forces a full rebuild.
set JEKYLL_CONFIG=_config.yml,_config.local.yml,_config.local.en.yml
set JEKYLL_CLEAN=0
for %%A in (%*) do (
    if /i "%%~A"=="all" set JEKYLL_CONFIG=_config.yml,_config.local.yml
    if /i "%%~A"=="clean" set JEKYLL_CLEAN=1
)

rem Walk up to the site root, so Jekyll is never started from the wrong folder.
set DEPTH=0
:findroot
if exist "_config.yml" goto foundroot
set /a DEPTH+=1
if %DEPTH% GEQ 10 goto notfound
cd ..
goto findroot

:notfound
echo Could not find _config.yml above "%~dp0" - put this .bat in or below the wiki folder.
pause
exit /b 1

:foundroot
echo Site root: %cd%
echo.

rem Jekyll 3 only loads the github-pages plugins (theme, markdown) when a file
rem named Gemfile is in the site root, so copy it there. It is git-ignored.
if not exist "Gemfile" copy /y ".env-files\Gemfile.github" "Gemfile" >nul
set BUNDLE_GEMFILE=%cd%\Gemfile

rem "clean" throws away the previous build, to force a full rebuild.
if "%JEKYLL_CLEAN%"=="1" (
    if exist "_site" rmdir /s /q "_site"
    if exist ".jekyll-metadata" del ".jekyll-metadata"
)

where git
where ruby
where bundle
if errorlevel 1 (
    echo.
    echo Bundler was not found. Install Ruby from https://rubyinstaller.org/ and run: gem install bundler
    pause
    exit /b 1
)
echo.

call bundle check >nul 2>nul
if errorlevel 1 (
    echo Installing gems...
    call bundle install
    if errorlevel 1 (
        echo.
        echo bundle install failed - see the messages above.
        pause
        exit /b 1
    )
    echo.
)

rem Stop an old server still holding the port, or it keeps serving the old build.
rem ":<port> " with the trailing space avoids matching ports such as 14000.
set FOUND_OLD=0
for /f "tokens=5" %%P in ('netstat -ano ^| findstr /c:":%JEKYLL_PORT% " ^| findstr /c:"LISTENING"') do (
    echo Stopping old server (PID %%P^)...
    taskkill /F /PID %%P >nul 2>nul
    set FOUND_OLD=1
)
if "%FOUND_OLD%"=="1" timeout /t 1 /nobreak >nul

echo Open http://localhost:%JEKYLL_PORT%%JEKYLL_BASEURL%/home when the server is ready. Press Ctrl+C to stop it.
echo.

rem Build first, so the total time can be printed, then serve what was built.
call bundle exec jekyll build --baseurl %JEKYLL_BASEURL% --config %JEKYLL_CONFIG% --incremental --verbose
if errorlevel 1 (
    echo.
    echo The build failed - see the messages above.
    pause
    exit /b 1
)

for /f %%T in ('ruby -e "print Time.now.to_i" 2^>nul') do set T_END=%%T
if defined T_START if defined T_END (
    set /a T_TOTAL=T_END-T_START
    set /a T_MIN=T_TOTAL/60
    set /a T_SEC=T_TOTAL%%60
)
echo.
if defined T_TOTAL echo Total time from start to finished build: %T_MIN% min %T_SEC% s (%T_TOTAL% seconds^)
if "%~1"=="" (echo Options used: none - English only, reusing the previous build) else (echo Options used: %*)
echo Open http://localhost:%JEKYLL_PORT%%JEKYLL_BASEURL%/home - press Ctrl+C to stop the server.
echo.

call bundle exec jekyll serve --skip-initial-build --host %JEKYLL_HOST% --port %JEKYLL_PORT% --baseurl %JEKYLL_BASEURL% --config %JEKYLL_CONFIG% --incremental --verbose
pause
