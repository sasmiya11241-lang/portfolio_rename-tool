import tkinter as tk

"""
ファイルを読み込んで、その名前を変更するファイル
次に名前の一部を変更する機能をつける

拡張として
・複数のファイルを読み込む
・指定した名前の部分を読みだす
・読みだした部分の名前を変更する

・tkinterを使って、GUIで動かせるようにする
"""

def mainwindow():

    root = tk.Tk()

    # 画面表示サイズ　横x縦+横の位置+縦の位置
    root.geometry('400x400+400+200')
    # タイトル名
    root.title('名前変更君')
    # 画面サイズ変更許可　今回は不可
    root.resizable(False,False)

    # ラベル
    label = tk.Label(root, text="名前変更アプリ")
    label.pack()

    # エントリー
    entry = tk.Entry(root)
    entry.pack()

    # ボタン
    button = tk.Button(root,text='変換実行' ,command=rename(new_name='goodbye'))
    button.pack()

    # これがないと画面が表示されない
    root.mainloop()


def rename(mode=0,old_name='defalt',new_name=''):

    """
    名前変更の処理

    変数一覧
    mode ← 変数に入れられた値によって動作する(名前を完全変更か一部変更)　予定
    old_name ←　変更前の名前
    new_name ←　変更後の名前

    """

    print(old_name)

    if new_name != '':
        print(f'{old_name}を{new_name}に変更します')
        old_name = new_name

def main():
    mainwindow()

if __name__ == "__main__":
    main()