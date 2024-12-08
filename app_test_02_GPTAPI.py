import streamlit as st
from PIL import Image
import requests

st.title('わし、藤井風')
st.caption('藤井風があなたに寄り添うアプリ')
st.subheader('かじぇの相談部屋')
st.text('わし風は、あんたの幸せをねがっちょるよ\n'
            'なんでも相談してみてな')
code = '''
import streamlit as st

st.title('わし、藤井風')
'''
st.code(code, language='python')

#画像
image = Image.open('main_img_202108.jpeg')
st.image(image, width=500)

#入力欄からカーソルが離れてもいちいちリロードしないようにwith句で設定
with st.form(key='profile_form'):
    #テキストボックス
    name =st.text_input('名前')
    address = st.text_input('住所')

    #セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('子ども', '大人'))

    #ラジオボタン
    age_category = st.radio(
        '年齢層',
        ('子ども', '大人'))

    #複数選択
    song = st.multiselect(
        '好きな曲',
        ('青春病', 'へでもねーよ', '旅路', 'きらり', '燃えよ','ガーデン', 'damn', 'grace', '花', '満ちてゆく', 'Feelin’ Go(o)d')
    )

    #ボタン
    submit_btn = st.form_submit_button('送信')
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        CHATGPT_API_KEY = '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'

        # ChatGPTでメッセージ生成
        def generate_message():
            prompt = "元気づけるメッセージを作ってください。#メッセージは250字以内 #口調は次のテキストを参考にしてください：この曲はねぇ、/あの2022年の飛行機の中で/サビのフレーズが浮かんで/2023、まぁそっから、でぇ、/まぁその時にちょっと/Ｌ…ロサンゼルスの方でデモを作って/で2023年にちょっと、/まぁ2023年ぐらいまで寝かしといて/2023年に、/なんかもっといい感じにしたいな/と思って作り直して/であの今年に入ってアレンジとか/し直した感じです。/んー、いやぁ、わしああいうの大好きなんすよ。/なんかああいう誰も傷つけないハプニング/大好きなんすよ。/だから、あれは神様のかわいいイタズラっすね。/これかなり気に入ってるんすよ。/この、シルバーというか、/金髪とはぼくは言ってないんすけど/シルバーというか白というか/そういう感じの色、気に入ってます。/アニメの歌、なんかわしマジで/「千と千尋」と「ちびまる子ちゃん」ぐらいしか通ってないんすよ、アニメ。/だから今はあんまり考えてないんですけど、/でもなんか勉強する機会があったらなんか/その時、なんか、好き…/なんかハマってみたいなぁと思うし…。/うん、わかんない。/犬。/なんか猫はちょっと何考えとんかわからんから/扱うのが、ちょっとわかんない。/扱い方が、あの…/何考えてるのかわからないですあの人たちは。/自信ですかね。/だからカッコ悪いときもいっぱいあります。/自信がないときですね。/だから一緒にカッコよくなりましょうよ。/なんか……深いところにある、なんか/深いところから生まれる自信みたいなのを/なんか頑張って身につけようぜ、って感じ。/一緒にカッコよくなろうぜ。/まだ、えー？なになに言う…/言ったらいんかわからんのやけど/んー、愛ですね、愛。/ちょっと今、/携帯片手に持っとるけんさぁ愛ができん。/オッケー、愛ですね。"
            
            headers = {
            'Authorization': f"Bearer {CHATGPT_API_KEY}",
            'Content-Type': 'application/json',
            }
            
            data = {
            "model": "gpt-4o",
            "messages": [{"role": "system", "content": "あなたは藤井風です"}, {"role": "user", "content":prompt}],
            }

            response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
            response_data = response.json()
            message = response_data['choices'][0]['message']['content']
            return message
        
        message = generate_message()
    
        st.text(f'ようこそ！{name}さん！{address}に限定版DVDを送ったで！')
        st.text(f'年齢層：{age_category}')
        st.text(f'好きな曲：{", ".join(song)}')
        st.text(f'メッセージ：{message}')