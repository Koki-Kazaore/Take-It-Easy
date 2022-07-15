  # 階段の段数
  all_steps = int(input())
  # 登ることのできる階段の数
  standardInput = [int(e) for e in input().split()]
  stepA = standardInput[0]
  stepB = standardInput[1]


  # 階段の状況をリスト表示 0段目も考慮するため+1する
  status = [0] * (all_steps + 1)
  # 現在値 
  current_point = 0

  while True:
    if current_point + stepB >= len(status):
      # loopの終了条件
      if current_point + stepA >= len(status):
        status[all_steps] = 1
        break

      # 踏んだ段に1を格納していく
      status[current_point + stepA] = 1
      current_point += status[current_point + 1:].index(1) + 1

    else:
      status[current_point + stepA] = 1
      status[current_point + stepB] = 1
      current_point += status[current_point + 1:].index(1) + 1
      # print(current_point)

    # Bの歩幅の範囲が全て踏まれていたらばそれ以降はすべての段を踏むという自明な場合は
    # 実行速度を早めるためにもすぐに終わらせる
    if status[stepB:stepB * 2] == [1] * stepB:
      status[current_point:] = [1] * (len(status) - current_point)
      break

  print(status.count(0) - 1)


  # 確認用テストコード
  #print("stepA:", stepA)
  #print("stepB:", stepB)
  #print("status:", status)
