main::IO()
main = do
    line_points <- getLine
    line_value <- getLine

    let points = read line_points :: Int
    let base_value = read line_value :: Int

    print (calculateLevel points base_value)

calculateLevel::Int -> Int -> Int
calculateLevel points base = countLevel points base 1

countLevel::Int -> Int -> Int -> Int
countLevel points base n
    | points - base < 0 = n
    | otherwise = countLevel (points - base) (base * 2) (n + 1)