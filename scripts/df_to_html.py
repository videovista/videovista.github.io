import pandas as pd
import re
def custom_to_html(df):
    # Convert the DataFrame to HTML
    df['Overall'] = df['Overall'].apply(lambda x: f"<b>{x}</b>")
    html_str = df.to_html(index=True, escape=False)

    # Replace <th> with <td>
    html_str = re.sub(r'<th>', '<td style="vertical-align: middle;">', html_str)
    html_str = re.sub(r'</th>', '</td>', html_str)

    # Add style attribute to <td>
    html_str = re.sub(r'<td>', '<td style="vertical-align: middle;">', html_str)
    
    # 每个模型都要进行依次替换  
    html_str = re.sub(r'<td style="vertical-align: middle;">GPT-4o</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://openai.com/index/hello-gpt-4o/" class="ext-link" style="font-size: 16px; margin-left: 5px;">GPT-4o', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">Gemini-1.5-Flash</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://storage.googleapis.com/deepmind-media/gemini/gemini_v1_5_report.pdf" class="ext-link" style="font-size: 16px; margin-left: 5px;">Gemini-1.5-Flash', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">PLLaVA</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/magic-research/PLLaVA" class="ext-link" style="font-size: 16px; margin-left: 5px;">PLLaVA', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">Uni-MoE</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://uni-moe.github.io/" class="ext-link" style="font-size: 16px; margin-left: 5px;">Uni-MoE', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">VideoChat2-Mistral</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/OpenGVLab/Ask-Anything/tree/main/video_chat2" class="ext-link" style="font-size: 16px; margin-left: 5px;">VideoChat2-Mistral', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">LLaMA-VID</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/dvlab-research/LLaMA-VID" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaMA-VID', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">LLaVA-NeXT-Video-DPO</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://llava-vl.github.io/blog/2024-04-30-llava-next-video/" class="ext-link" style="font-size: 16px; margin-left: 5px;">LLaVA-NeXT-Video-DPO', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">Video-LLaVA</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/PKU-YuanGroup/Video-LLaVA" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-LLaVA', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">VILA-1.5</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/NVlabs/VILA" class="ext-link" style="font-size: 16px; margin-left: 5px;">VILA-1.5', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">VideoChat2-Vicuna</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/OpenGVLab/Ask-Anything/tree/main/video_chat2" class="ext-link" style="font-size: 16px; margin-left: 5px;">VideoChat2-Vicuna', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">ShareGPT4Video</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/ShareGPT4Omni/ShareGPT4Video" class="ext-link" style="font-size: 16px; margin-left: 5px;">ShareGPT4Video', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">IVA</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://arxiv.org/pdf/2402.13546" class="ext-link" style="font-size: 16px; margin-left: 5px;">IVA', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">Video-ChatGPT</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/mbzuai-oryx/Video-ChatGPT" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-ChatGPT', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">Video-LLaMA</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/DAMO-NLP-SG/Video-LLaMA" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-LLaMA', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">VideoChat_with_ChatGPT</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/OpenGVLab/Ask-Anything/tree/main/video_chat_with_ChatGPT" class="ext-link" style="font-size: 16px; margin-left: 5px;">VideoChat_with_ChatGPT', html_str)
    
    
    html_str = re.sub(r'<td style="vertical-align: middle;">Video-CCAM</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/QQ-MM/Video-CCAM" class="ext-link" style="font-size: 16px; margin-left: 5px;">Video-CCAM', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">VideoLLaMA2</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/DAMO-NLP-SG/VideoLLaMA2" class="ext-link" style="font-size: 16px; margin-left: 5px;">VideoLLaMA2', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">VTimeLLM-Vicuna</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/huangb23/VTimeLLM" class="ext-link" style="font-size: 16px; margin-left: 5px;">VTimeLLM-Vicuna', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">VTimeLLM-ChatGLM</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/huangb23/VTimeLLM" class="ext-link" style="font-size: 16px; margin-left: 5px;">VTimeLLM-ChatGLM', html_str)
    html_str = re.sub(r'<td style="vertical-align: middle;">MiniGPT4-Video</td>', '<td style="text-align: left; padding: 2px 10px; vertical-align: middle;"><b class=""><a href="https://github.com/Vision-CAIR/MiniGPT4-video" class="ext-link" style="font-size: 16px; margin-left: 5px;">MiniGPT4-Video', html_str)
    return html_str

# 创建数据
data = {
    "Model": ["VideoChat_with_ChatGPT", "Video-LLaMA", "Video-ChatGPT", "IVA", "ShareGPT4Video", "VILA-1.5",
              "Video-LLaVA", "LLaMA-VID", "LLaVA-NeXT-Video-DPO", "VideoChat2-Vicuna", "VideoChat2-Mistral", 
              "PLLaVA", "PLLaVA", "Uni-MoE", "Gemini-1.5-Flash", "GPT-4o", "place"],
    "Language Model": ["gpt-3.5-turbo", "Vicuna-7B", "Vicuna-7B", "Vicuna-7B", "Vicuna-7B", "Llama3-8B",
                       "Vicuna-7B", "Vicuna-7B", "Vicuna-7B", "Vicuna-7B", "Mistral-7B", "Vicuna-7B", 
                       "Vicuna-13B", "Vicuna-7B", "Gemini", "GPT-4", "place"],
    "Frames": [40, 16, 100, 200, 16, 8, 8, "1 fps", 16, 16, 16, 16, 16, 8, "1 fps", 100, 1],
    "Date": ["2024-07-05", "2024-07-05", "2024-07-05", "2024-07-05", "2024-07-05", "2024-07-05", "2024-07-05", "2024-07-05", "2024-07-05", "2024-07-05" ,"2024-07-05" ,"2024-07-05" ,"2024-07-05" ,"2024-07-05" ,"2024-07-05" ,"2024-07-05", ""],
    "Overall": [17.99, 25.35, 36.65, 39.70, 53.58, 55.15, 56.59, 56.87, 56.66, 53.64, 57.24, 60.36, 64.67, 61.13, 76.39, 78.26, 100],
    "Unders.": [16.64, 25.40, 36.09, 37.38, 51.79, 52.99, 53.82, 54.00, 54.12, 51.79, 54.91, 58.35, 62.44, 58.65, 74.73, 75.15, 100],
    "Reason.": [23.04, 25.16, 38.73, 48.38, 60.30, 63.24, 66.91, 67.61, 66.14, 60.55, 65.95, 67.86, 73.00, 69.62, 82.30, 87.97, 100],

}

# 创建 DataFrame
df = pd.DataFrame(data)

# 示例：添加新行
# new_data = {"Model": "NewModel", "Language Model": "NewLanguageModel", "Frames": 50, "Unders.": 60.00, "Reason.": 70.00, "Overall": 65.00}
# df = df.append(new_data, ignore_index=True)
new_data = [
  {"Model": "Video-CCAM", "Language Model": "Yi-1.5-9B", "Frames": 96, "Unders.": 62.40, "Reason.": 71.84, "Overall": 64.39, "Date": "2024-07-05"},
  {"Model": "VideoLLaMA2", "Language Model": "Mistral-7B", "Frames": 16, "Unders.": 58.73, "Reason.": 66.97, "Overall": 60.47, "Date": "2024-07-05"},
  {"Model": "MiniGPT4-Video", "Language Model": "Mistral-7B", "Frames": 45, "Unders.": 51.73, "Reason.": 65.50, "Overall": 54.64, "Date": "2024-07-05"},
  {"Model": "VILA-1.5", "Language Model": "Vicuna-13B", "Frames": 8, "Unders.": 62.27, "Reason.": 71.34, "Overall": 64.18, "Date": "2024-07-07"},
  {"Model": "VTimeLLM-Vicuna", "Language Model": "Vicuna-7B", "Frames": 100, "Unders.": 52.24, "Reason.": 63.07, "Overall": 54.52, "Date": "2024-07-07"},
  {"Model": "VTimeLLM-ChatGLM", "Language Model": "ChatGLM3-6B", "Frames": 100, "Unders.": 50.91, "Reason.": 60.15, "Overall": 52.86, "Date": "2024-07-07"}
  ]

for d in new_data:
  df = df.append(d, ignore_index=True)

# 按 Overall 列排序
df = df.sort_values(by="Overall", ascending=False).reset_index(drop=True)

print(df)

# html_table = df.to_html(index=True, classes='js-sort-table', table_id='results')
html_table = custom_to_html(df)
html_template = f'''
<h2 class="title is-3" id="leaderboard">Leaderboard on VideoVista</h2>
<div class="content">
  <p class="mt-3">Accuracy scores on the VideoVista Dataset.</p>
  <p><b>Unders.</b>(Video Understanding Task); <b>Reason.</b>(Video Reasoning Task)</p>
  {html_table}
</div>
'''
print(html_template)


