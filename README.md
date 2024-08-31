# fastPipeline

# fastPipeline

fastPipeline 是一个用于快速处理数据的管道工具。它提供了一系列功能来读取、处理和写入数据，并且支持日志记录以便于调试和监控。

## 功能介绍

- **读取输入文件**：从指定的 JSON 文件中读取数据。
- **处理数据**：根据自定义的逻辑对数据进行处理。
- **写入输出文件**：将处理后的数据写入到指定的 JSON 文件中。
- **日志记录**：记录处理过程中的重要信息，包括错误信息，方便排查问题。

## 使用方法

1. **准备输入文件**：在 `source/test001/index001/input.json` 或 `source/test001/index002/input.json` 中准备好要处理的 JSON 数据。
2. **运行脚本**：使用 `start.sh` 启动服务，或者直接运行 `index001.py` 或 `index002.py` 脚本。
   ```sh
   uvicorn --host 0.0.0.0 --port 8000 main:app --reload
   ```
   或者
   ```sh
   python source/test001/index001/index001.py -input_file_path <输入文件路径> -output_file_path <输出文件路径> -log_file_path <日志文件路径>
   ```
3. **查看日志**：日志文件会记录在指定的路径中，可以查看处理过程中的详细信息。

## 示例

假设你有一个输入文件 `input.json`，内容如下：
```json
{
    "name": "example",
    "value": 42
}
运行以下命令来处理数据：

```sh
python source/test001/index001/index001.py -input_file_path source/test001/index001/input.json -output_file_path source/test001/index001/output.json -log_file_path source/test001/index001/log.txt
```

处理完成后，你可以在 `output.json` 中看到处理后的数据。

## 注意事项

- 确保输入文件路径和输出文件路径正确，否则会导致文件读取或写入失败。
- 日志文件路径默认在 `source/test001/index001/log.txt`，如果需要修改，可以在脚本中进行调整。

## 更新日志


