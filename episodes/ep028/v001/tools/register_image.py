from pathlib import Path
import argparse, hashlib, json, shutil

root = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser()
parser.add_argument('shot_id', type=int)
parser.add_argument('generated_file', type=Path)
a = parser.parse_args()
source = a.generated_file.resolve()
if not source.is_file():
    raise SystemExit(f'Image does not exist: {source}')
shot_id = a.shot_id
prompt_file = root / 'prompts' / f'shot_{shot_id:02}.json'
ref_file = root / 'references' / f'shot_{shot_id:02}.json'
dest = root / 'images' / f'shot_{shot_id:02}.png'
shutil.copy2(source, dest)
prompt = json.loads(prompt_file.read_text())
metadata = {
    'shot_id': shot_id,
    'source': 'image_gen',
    'generated_file': str(source),
    'prompt_sha256': hashlib.sha256(prompt_file.read_bytes()).hexdigest(),
    'reference_manifest': f'references/shot_{shot_id:02}.json',
    'reference_manifest_sha256': hashlib.sha256(ref_file.read_bytes()).hexdigest(),
    'sha256': hashlib.sha256(dest.read_bytes()).hexdigest(),
}
(dest.with_suffix('.source.json')).write_text(json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
board_file = root / 'storyboard.json'
board = json.loads(board_file.read_text())
board['shots'][shot_id]['image_status'] = 'generated'
board_file.write_text(json.dumps(board, ensure_ascii=False, indent=2) + '\n')
print(json.dumps(metadata, ensure_ascii=False))
