loop do
  n = gets.chomp.to_i
  break if n == 0
  a_score = 0
  b_score = 0
  n.times do
    a, b = gets.chomp.split.map(&:to_i)
    if a > b
      a_score += a + b
    elsif a < b
      b_score += a + b
    else
      a_score += a
      b_score += b
    end
  end
  puts "#{a_score} #{b_score}"
end
