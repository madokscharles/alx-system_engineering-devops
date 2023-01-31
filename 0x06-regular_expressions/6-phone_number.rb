#!/usr/bin/env ruby
# Regular expression that must match a 10 digit phoone number
puts ARGV[0].scan(/^\d{10,10}$/).join
