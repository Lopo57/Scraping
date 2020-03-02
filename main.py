import sys
import scraping as SC

def main():

    args = sys.argv     #引数の受け取り
                            #[1]スクレイピング先URL
                            #[2]検索キーワード
                            #[3]ページ数指定用URL
                            #[4]画像出力先ディレクトリ

    Initialize(args)    #初期化

    for page_num in range(1, 5):

        g_cls_sc.GetHtmlSouce(page_num)     #ページ指定をしてHTMLを取得    


    Finalize()          #終了処理


def Initialize(args):
    global g_cls_sc                                     #グローバル化
    g_cls_sc = SC.Scraping(args[1], args[2], args[3], args[4])   #インスタンス生成

def Finalize():
    del g_cls_sc


if __name__ == '__main__':
    main()
