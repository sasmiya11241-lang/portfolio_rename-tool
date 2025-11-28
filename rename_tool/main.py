import tkinter as tk
from tkinter import filedialog, messagebox


"""
ファイルを読み込んで、その名前を変更するファイル
次に名前の一部を変更する機能をつける

拡張として
・複数のファイルを読み込む
・指定した名前の部分を読みだす
・読みだした部分の名前を変更する

・tkinterを使って、GUIで動かせるようにする
"""
'''
やること
grid()の中の行列をいじってボタン配列を綺麗にする
変数はinitにまとめて、コードをすっきりさせる
ボタン処理を作る
'''

# -------------処理-------------

class App:

    def __init__(self, root):
        # クラスの内部変数として保存
        self.root = root
        # 入力欄の生成
        self.entry_path = tk.Entry(root)
        self.new_name = tk.Entry(root)

        # 画面作成
        self.main_window()


    def choose_file(self):
        # ファイル選択ダイアログを開く（初期ディレクトリはカレント）
        path = filedialog.askopenfilename(title="名前を変更するファイルを選択")
        if path:
            # 選ばれたパスを entry に表示
            self.entry_path.delete(0, tk.END) # entryの名前を消す
            self.entry_path.insert(0, path)
        else:
            # キャンセルしたときは何もしない（任意）
            pass

        return



    def rename(self,mode=0,old_name='default'):

        """
        名前変更の処理

        変数一覧
        mode ← 変数に入れられた値によって動作する(名前を完全変更か一部変更)　予定
        old_name ←　変更前の名前
        new_name ←　変更後の名前

        """

        print(f'renameが動作します')
        print(f'{old_name}')
        new_name = self.new_name.get()

        if new_name != '':
            print(f'{old_name}を{new_name}に変更します')
            old_name = new_name

    # -------------画面-------------

    def main_window(self):

        # 画面表示サイズ　横x縦+横の位置+縦の位置
        self.root.geometry('400x400+400+200')

        # タイトル名
        self.root.title('名前変更君')

        # 画面サイズ変更許可　今回は不可
        self.root.resizable(False,False)

        # ラベル
        label = tk.Label(self.root, text="名前変更アプリ")
        label.grid(row=0, column=1, padx=10, pady=5)

        # 入力欄の配置
        self.entry_path.grid(row=1, column=0, padx=10, pady=5)

        # ファイル選択ボタン
        btn = tk.Button(self.root, text="選択", command=self.choose_file)
        btn.grid(row=1, column=1, padx=10, pady=5)

        # 新しい名前の入力
        self.new_name.grid(row=2, column=0, padx=10, pady=5)

        # 変換実行ボタン
        # command=lambda: 関数名()　この形にしないと起動と同時にボタンが実行する
        button = tk.Button(self.root, text='変換実行', command=lambda: self.rename())
        button.grid(row=2, column=1, padx=10, pady=5)

def main():
    root = tk.Tk()
    app = App(root)

    # これがないと画面が表示されない
    root.mainloop()

if __name__ == "__main__":
    # このプログラムが実行されたときにmain()を実行する パッケージとして呼び出されるときは実行しない
    main()