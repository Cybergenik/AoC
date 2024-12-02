defmodule Day1 do

  def part1 do
    File.stream!("input.txt")
    |> Stream.map(fn line -> 
      [l, r] = String.split(String.trim(line), "   ")
      {String.to_integer(l), String.to_integer(r)}
    end)
    |> Enum.unzip()
    |> then(fn {ll, rl} ->
      Enum.zip(Enum.sort(ll), Enum.sort(rl))
    end)
    |> Enum.reduce(0, fn {l, r}, total ->
      total + abs(l - r)
    end)
    |> IO.puts
  end

  def part2 do
    File.stream!("input.txt")
    |> Stream.map(fn line -> 
      [l, r] = String.split(String.trim(line), "   ")
      {String.to_integer(l), String.to_integer(r)}
    end)
    |> Enum.unzip()
    |> then(fn {ll, rl} ->
      rc = Enum.frequencies(rl)
      ll 
      |> Enum.sort()
      |> Enum.reduce(0, fn l, total ->
        total + l * Map.get(rc, l, 0)
      end)
    end)
    |> IO.puts
  end
end

Day1.part1()
Day1.part2()
