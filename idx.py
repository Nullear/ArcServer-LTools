import json
import argparse
from typing import Dict, Any, List

your_slst_directory = 'Your/songlist'

def add_index_to_songs(json_data: Dict[str, Any]) -> Dict[str, Any]:
    
    if "songs" not in json_data or not isinstance(json_data["songs"], list):
        raise ValueError("JSON数据中未找到songs数组或songs不是数组类型")
    
    songs = json_data["songs"]
    for idx, song in enumerate(songs):
    
        new_song = {"idx": idx}
        new_song.update(song)
        songs[idx] = new_song
    return json_data

def process_json_file(input_file: str, output_file: str = None) -> None:
    
    if output_file is None:
        output_file = input_file.rsplit('.', 1)[0] + '_with_idx.json' if '.' in input_file else input_file + '_with_idx.json'
    
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            json_data = json.load(f)
        
        modified_data = add_index_to_songs(json_data)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            
            json.dump(modified_data, f, ensure_ascii=False, indent=4)
        
        print(f"处理完成，已保存到 {output_file}")
    
    except FileNotFoundError:
        print(f"错误：找不到输入文件 {input_file}")
    except json.JSONDecodeError:
        print(f"错误：无法解析JSON文件 {input_file}")
    except ValueError as e:
        print(f"错误：{e}")
    except Exception as e:
        print(f"发生未知错误：{e}")

if __name__ == "__main__":
    process_json_file(your_slst_directory, 'songlist')
