import unittest
from unittest.mock import patch
import main


# テストケースクラスを作成
class TestIpMonitor(unittest.TestCase):
    # テスト前の初期設定
    def setUp(self):
        # テスト用のIPアドレスを設定
        self.ip_data = "123.456.789.012"
        # ip.txtファイルにテスト用のIPアドレスを書き込む
        with open("ip.txt", "w") as f:
            f.write(self.ip_data)

    # IPアドレスの取得と比較のテスト
    @patch("requests.get")
    def test_ip_check(self, mock_get):
        # requests.getの戻り値をモック化
        mock_get.return_value.json.return_value = {"origin": self.ip_data}
        # IPアドレスのチェックを実行
        main.check_ip()
        with self.subTest("IPアドレスが正しく取得できていることを確認"):
            self.assertEqual(main.ip_res["origin"], self.ip_data)


# テストを実行
if __name__ == "__main__":
    unittest.main()
