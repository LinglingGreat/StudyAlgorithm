N = 20

@memo = {1 => 1}
def set_tap(remain)
  return @memo[remain] if @memo.has_key?(remain)
  cnt = 0
  # 2插口
  (1..(remain / 2)).each{|i|
    if remain - i == i then
      cnt += set_tap(i) * (set_tap(i) + 1) / 2
    else
      cnt += set_tap(remain - i) * set_tap(i)
    end
  }
  # 3插口
  (1..(remain / 3)).each{|i|
    (i..((remain - i) / 2)).each{|j|
      if (remain - (i + j) == i) && (i == j) then
        cnt += set_tap(i) * (set_tap(i) + 1) * (set_tap(i) + 2) / 6
      elsif remain - (i + j) == i then
        cnt += set_tap(i) * (set_tap(i) + 1) * set_tap(j) / 2
      elsif i == j  then
        cnt += set_tap(remain - (i+j)) * set_tap(i) * (set_tap(i)+1) / 2
      elsif remain - (i + j) == j then
        cnt += set_tap(j) * (set_tap(j) + 1) * set_tap(i) / 2
      else
        cnt += set_tap(remain - (i + j)) * set_tap(j) * set_tap(i)
      end
    }
  }
  @memo[remain] = cnt
end

puts set_tap(N)
