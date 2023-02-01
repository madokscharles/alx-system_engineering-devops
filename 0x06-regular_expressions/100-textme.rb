#!/usr/bin/env ruby
# Regular expressions
puts ARGV[0].scan(/\[from:(.*)\].*\[to:(.*)\].*\[flags:(.*?)\]/).join(",")
