n = 5

# 顺序搜索的初始值
fw = [(1..n*2).to_a]
# 逆序搜索的初始值
bw = [(1..n*2).to_a.reverse]

depth = 1
while true do
  # 顺序搜索
  fw = fw.each_with_object([]) do |c, result|
    1.upto(n){|i| result << c[i, n] + c[0, i] + c[i + n..-1]}
  end
  break if (fw & bw).size > 0
  depth += 1

  # 逆序搜索
  bw = bw.each_with_object([]) do |c, result|
    1.upto(n){|i| result << c[n, i] + c[0, n] + c[i + n..-1]}
  end
  break if (fw & bw).size > 0
  depth += 1
end

puts depth
