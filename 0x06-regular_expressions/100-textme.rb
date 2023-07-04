#!/usr/bin/env ruby
# A regular expression that is matches a given pattern
puts ARGV[0].scan(/\[from:(\+?(?:\w)+)\]\s\[to:(\+?(?:\w)+)\]\s\[flags:((?:-?\d:?)+)\]/).join(separator=",")
