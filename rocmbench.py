import argparse
import time
import sys
import torch

def get_vram_usage():
    """PyTorch の torch.cuda.mem_get_info() を用いてVRAM使用率を計算（単一GPUの場合）"""
    try:
        free_mem, total_mem = torch.cuda.mem_get_info()
        used_mem = total_mem - free_mem
        usage = (used_mem / total_mem) * 100.0
        return usage
    except Exception as e:
        # GPUが利用できない場合などは None を返す
        return None

def main():
    parser = argparse.ArgumentParser(
        description="ROCm PyTorch Power Loading Script (Load parameters in percentage)"
    )
    parser.add_argument('--load', type=int, default=80,
                        help="Target GPU load percentage (default: 80)")
    parser.add_argument('--vram', type=int, default=80,
                        help="Target VRAM load percentage (default: 80)")
    parser.add_argument('--duration', type=int, default=5,
                        help="Loading duration in minutes (default: 5)")
    args = parser.parse_args()

    # パラメータの妥当性チェック
    if not (0 <= args.load <= 100):
        sys.exit("Error: --load must be between 0 and 100.")
    if not (0 <= args.vram <= 100):
        sys.exit("Error: --vram must be between 0 and 100.")
    if args.duration <= 0:
        sys.exit("Error: --duration must be a positive number.")

    print(f"Starting ROCm power loading test with:")
    print(f"  GPU Load: {args.load}%")
    print(f"  VRAM Load: {args.vram}%")
    print(f"  Duration: {args.duration} minute(s)")

    # 以下はサンプルの疑似負荷処理：進捗バーと同時にVRAM使用率を更新表示する
    total_time_sec = args.duration * 60
    update_interval = 0.1  # 0.1秒ごとに更新
    total_steps = int(total_time_sec / update_interval)
    
    for i in range(total_steps):
        progress = (i / total_steps) * 100
        # GPU VRAM使用率の取得
        vram_usage = get_vram_usage()
        vram_str = f"{vram_usage:5.1f}%" if vram_usage is not None else "N/A"
        bar_length = 50
        filled_length = int(bar_length * progress // 100)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)
        # 例: "|███████████████████████████████████████-------| 86.7% Complete, VRAM Usage: 80.0%"
        print(f"|{bar}| {progress:5.1f}% Complete, VRAM Usage: {vram_str}", end='\r')
        time.sleep(update_interval)
    
    print("\nTest completed.")

if __name__ == "__main__":
    main()
