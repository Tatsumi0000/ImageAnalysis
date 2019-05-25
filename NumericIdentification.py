import cv2
import numpy as np


class NumericIdentification:
    """
    画像から数字を判別

    Attributes
    ----------
    img : np.ndarray
      解析画像を多次元配列にしたもの
    img_gray : np.ndarray
      imgをグレースケールしたもの
  """

    def __init__(self, img_path="./img/input.jpg"):
        """
      コンストラクタ

      Parameters
      ----------
      img_path : str
        解析する画像のパス
    """
        # 画像を読み込む
        self.img = cv2.imread(img_path)
        # グレースケール化（画像の2値化はグレースケールでないとダメ）
        self.img_gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        # self.debug_show(self.img_gray)

    def image_cut(self, col1, col2, row1, row2) -> np.ndarray:
        """
      画像を切り出すメソッド

      Parameters
      ----------
      col1 : int
        切取り開始のy座標
      col2 : int
        切取り終了のy座標
      row1 : int
        切取り開始のx座標
      row2 : int
        切取り終了のx座標

      Returns
      -------
      cut_img : np.ndarray
       引数で受け取った座標を切り取った画像（numpyの多次元配列）
    """
        cut_img = self.img_gray[col1: col2, row1: row2]
        return cut_img

    def binarization(self, threshold=80):
        """
      画像を2値化するメソッド
      2値化する画像は必ずグレースケールした画像でなければならない

      Parameters
      ----------
      threshold : int
        しきい値デフォルトでは80

      Attributes
      ----------
      ret : int
        設定した閾値（下の大津の2値化は嘘かも）
        大津の二値化（2値化した際にクラス0とクラス1に分割する．その際に各クラスの平均を求めその中間を計算した数字といったようなイメージ）
      th : np.ndarray
        2値化した画像の多次元配列
    """
        ret, th = cv2.threshold(self.image_cut(260, 490, 0, 300), threshold, 255, cv2.THRESH_BINARY)
        self.debug_show(th)
        # print("{0}".format(ret))

    def debug_show(self, show_img):
        """デバッグ用のために画像を表示するメソッド
    """
        cv2.imshow("DEBUG NOW...", show_img)
        cv2.waitKey()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    numeric_identification = NumericIdentification()
    a = numeric_identification.image_cut(260, 490, 0, 300)
    numeric_identification.binarization()
