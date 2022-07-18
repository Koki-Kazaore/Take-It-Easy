# hello, world

# 右下へ進む
      for buttom_right in range(i + 1, size):
        # 前回値より1大きい場合
        if matrix[buttom_right - 1][buttom_right - i - 1] == matrix[buttom_right][buttom_right - i] - 1:
          temp_swipes += 1