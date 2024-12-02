defmodule Day2 do

  defp deps do
    [
      {:benchee, "~> 1.0"}
    ]
  end

  def benchmark do
    Benchee.run(%{
      "part1" => fn -> part1() end,
      "part2" => fn -> part2() end
    })
  end

  def results do
    IO.puts("Part 1: #{part1()}")
    IO.puts("Part 2: #{part2()}")
  end

  def check_seq(li) when is_list(li) do
    Enum.zip(li, tl(li))
    |> Enum.reduce_while({-1, true}, fn {n1, n2}, {incr, _} ->
      # Check increment
      new_incr =
        cond do
          n1 < n2 -> if incr == -1, do: 1, else: if incr == 0, do: :error, else: 1
          n1 > n2 -> if incr == -1, do: 0, else: if incr == 1, do: :error, else: 0
          true -> :error
        end

      # Stop early if invalid
      if new_incr == :error or abs(n1 - n2) not in 1..3 do
        {:halt, {incr, false}}
      else
        {:cont, {new_incr, true}}
      end
    end)
    |> elem(1)
  end

  def part1 do
    File.stream!("input.txt")
    |> Stream.map(&String.trim/1)
    |> Stream.map(&String.split(&1, " ", trim: true))
    |> Enum.reduce(0, fn li, total ->
      if check_seq(Enum.map(li, &String.to_integer/1)), do: total + 1, else: total
    end)
  end

  def part2 do
    File.stream!("input.txt")
    |> Stream.map(&String.trim/1)
    |> Stream.map(&String.split(&1, " ", trim: true))
    |> Enum.reduce(0, fn li, total ->
      if check_seq(Enum.map(li, &String.to_integer/1)) do
        total + 1
      else
        if Enum.any?(0..length(li)-1, fn i -> check_seq(Enum.map(List.delete_at(li, i), &String.to_integer/1)) end) do
          total + 1
        else
          total
        end
      end
    end)
  end
end

Day2.benchmark()
Day2.results()
