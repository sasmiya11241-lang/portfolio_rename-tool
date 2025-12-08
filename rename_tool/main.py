import tkinter as tk
from tkinter import filedialog, messagebox
import os


class FileRenamerModel:  # ロジック（Model）

    def rename(self, old_path, new_name):
        """ ファイル名を変更し、成功またはエラーを返す """

        if not old_path or not new_name:
            # Controller側で警告を出すため、ここでは単にNoneを返す
            return None, "エラー: ファイルと新しい名前を入力してください"

        # ファイルのディレクトリと拡張子を分割
        dir_name = os.path.dirname(old_path)
        ext = os.path.splitext(old_path)[1]
        new_path = os.path.join(dir_name, new_name + ext)

        try:
            os.rename(old_path, new_path)
            # 成功した場合は新しいパスを返す
            return new_path, None
        except Exception as e:
            # エラーが発生した場合はエラーメッセージを返す
            return None, str(e)


class RenamerController:  # 司令塔（Controller）

    def __init__(self, root):
        # 1. Modelのインスタンスを作成
        self.model = FileRenamerModel()

        # 2. Viewのインスタンスを作成し、ViewにController自身を渡す
        #    => これにより、ViewのボタンがControllerのメソッドを呼び出せるようになる
        self.view = RenamerView(root, self)

    def handle_choose_file(self):
        """ ファイル選択ボタンが押されたときの処理 """
        path = filedialog.askopenfilename(title="名前を変更するファイルを選択")
        if path:
            # ViewのEntryにパスをセットする
            self.view.entry_path.delete(0, tk.END)
            self.view.entry_path.insert(0, path)

    def handle_rename(self):
        """ 変換実行ボタンが押されたときの処理 """
        # 1. Viewからデータを取得
        old_path = self.view.entry_path.get()
        new_name = self.view.entry_new_name.get()

        # 2. Modelに処理を依頼
        new_path, error_message = self.model.rename(old_path, new_name)

        # 3. 結果をViewに反映（ユーザーへのフィードバック）
        if error_message:
            # エラーの場合はメッセージボックスを表示
            if "警告" in error_message:
                messagebox.showwarning("警告", error_message.split(":")[1].strip())
            else:
                messagebox.showerror("エラー", error_message)
        else:
            # 成功の場合はEntryを更新し、成功メッセージを表示
            messagebox.showinfo("成功", f"{old_path} を {new_path} に変更しました")
            self.view.entry_path.delete(0, tk.END)
            self.view.entry_path.insert(0, new_path)


class RenamerView:  # 見た目（View）

    def __init__(self, root, controller):
        self.root = root
        # Controllerのインスタンスを受け取り保存
        self.controller = controller

        # エントリー欄の生成
        self.entry_path = tk.Entry(root)
        self.entry_new_name = tk.Entry(root)

        # 画面作成
        self.main_window()

    def main_window(self):
        # 画面設定は省略
        self.root.geometry('400x400+400+200')
        self.root.title('名前変更君')
        self.root.resizable(False, False)

        # ラベル
        label = tk.Label(self.root, text="名前変更アプリ")
        label.grid(row=0, column=1)

        # 入力欄の配置
        self.entry_path.grid(row=1, column=0, padx=10, pady=5)

        # ファイル選択ボタン
        # ボタンのcommandは、Controllerのメソッドに紐付けられる
        btn = tk.Button(self.root, text="選択", command=self.controller.handle_choose_file)
        btn.grid(row=1, column=1, padx=10, pady=5)

        # 新しい名前の入力
        self.entry_new_name.grid(row=2, column=0, padx=10, pady=5)

        # 変換実行ボタン
        # ボタンのcommandは、Controllerのメソッドに紐付けられる
        button = tk.Button(self.root, text='変換実行', command=self.controller.handle_rename)
        button.grid(row=2, column=1, padx=10, pady=5)


def main():
    root = tk.Tk()
    # Controllerをインスタンス化する
    app = RenamerController(root)
    root.mainloop()


if __name__ == "__main__":
    main()