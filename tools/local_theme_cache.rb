# Local builds only: keeps the theme in .theme-cache so unchanged pages are skipped.
theme_cache = File.expand_path("../.theme-cache", __dir__)
seen = 0
patch = TracePoint.new(:end) do |tp|
  case tp.self.name
  when "Jekyll::RemoteTheme::Theme"
    tp.self.prepend(Module.new do
      define_method(:root) do
        require "fileutils"
        FileUtils.mkdir_p(theme_cache)
        @root ||= File.realpath(theme_cache)
      end
    end)
    seen += 1
  when "Jekyll::RemoteTheme::Munger"
    tp.self.prepend(Module.new { define_method(:enqueue_theme_cleanup) { nil } })
    seen += 1
  end
  patch.disable if seen == 2
end
patch.enable
