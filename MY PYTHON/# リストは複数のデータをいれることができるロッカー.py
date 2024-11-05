# リストは複数のデータをいれることができるロッカー
# リストには住所が存在する　住所＝インデックス(番号)＝番号ー１　最初は０から始める
# リストは鍵括弧で括る
a=["sato","suzuki","takahasi"]

a[1]="tanaka"

print(a[0])
print(a[1])
print(a[2])

a=[["sato","suzuki"],["takahasi","tanaka"]]

# satoサンは1つ目の1番目なので０，０になる
print(a[0][0]) 
print(a[0][1])
print(a[1][0])
print(a[1][1])
