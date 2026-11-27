# 主页文案修改指南

主页上的字和图分布在这几个地方：

- `README.md`：除示波器和厂商 logo 以外的所有文字。文件里带 ✏️ 的注释标出了每一处可以改的地方。
- `tools/scope.py`：示波器图上的文字，都在文件顶部的 `TEXT` 里。改完在仓库根目录运行 `python tools/scope.py`，深色和浅色两张图会一起重新生成。
- `tools/tech_stack.py`：技术栈三行的所有图标，以及鼠标悬停在图标上时浮出的说明文字，都在文件顶部的 `ROWS` 里。logo 图片放在 `assets/logos/`。改完运行 `python tools/tech_stack.py`，它会生成图标并自动重写 `README.md` 里的技术栈区块，不用手改 README。
- `assets/boards/`：硬件区的 6 张实拍抠图，600 × 440 透明底。换图时保持同样尺寸，板子大小看起来才一致。

改完以后，在 GitHub 网页上打开 `README.md`，点铅笔进入编辑，再切到 Preview 标签就能先看效果。

## 全部文案

| 位置 | 现在的内容 | 改哪里 |
|---|---|---|
| 顶部横幅大字 | Alvin Li | `README.md` 开头「顶部横幅」注释下面的 `text=`，深色、浅色、兜底三条都要改 |
| 顶部横幅小字 | Robotics × Full-stack · iRidium Lab | 同上，改 `desc=` |
| 蓝色打字动画（3 行轮播） | Robotics × Full-stack engineer / MCU · PCB · Control · Sensor Fusion / Tauri + Rust + React desktop tools | `README.md`「打字动画」注释下面的 `lines=`，写法见那段注释 |
| 打字动画下的中文 | 机器人系统硬件 · 嵌入式 · 姿态控制 · 传感器融合 \| 硬件为主，软件随行 | `README.md`「打字动画下面那行中文小字」注释下面 |
| 两个徽章 | iRidium Lab · my website / LinkedIn · Alvin Li | `README.md`「两个徽章」注释下面，`badge/` 后面是「左边文字-右边文字-颜色」：空格写 `_`，减号写 `--`，下划线写 `__` |
| 示波器机身左上角 | 无（留空就不显示） | `tools/scope.py` 的 `TEXT["brand"]`、`TEXT["model"]` |
| 示波器屏幕顶栏 | iRidium / RUN / H 2023 → NOW / Delay 0.00s / 1 GSa/s 14 Mpts | `TEXT["status_tag"]`、`TEXT["status"]`、`TEXT["status_right"]` |
| 示波器屏幕右栏 | iRidium / LAB / ROBOTICS × FULL-STACK | `TEXT["title"]`、`TEXT["title_sub"]`、`TEXT["title_tag"]` |
| 示波器三个通道 | CH1 HARDWARE / CH2 FIRMWARE / CH3 SOFTWARE | `TEXT["channels"]`；改了以后 `README.md` 里示波器 `<img alt=…>` 的通道名要手动改 |
| 示波器触发 | TRIG CH1 ↑ | `TEXT["trigger"]` |
| 示波器屏幕底部菜单（第 1 页） | MCU / PCB / CONTROL / SENSOR FUSION / WEB & AI / 1/2 ▸ | `TEXT["menu"]` |
| 示波器屏幕底部菜单（第 2 页，每 5 秒和第 1 页轮换） | DECODE / UART·RS232 / I2C / CAN·Modbus / SPI·1-Wire / 2/2 ◂ | `TEXT["decode"]`，一格里用 `\n` 分上下两行 |
| About | Robotic-systems hardware and embedded engineer. … | `README.md`「About」一节 |
| 硬件卡片 | GaN Quadrotor ESC、AD831 Active Mixer、Claude Chime Power Board、Cirro Cooling Controllers、Course Project Tool Boards、Wireless Voice-Controlled Light | `README.md`「Hardware」一节，`<b>` 是标题，`<sub>` 是说明；语音灯那张还没有作品集页面，所以没加链接 |
| 技术栈第一行（语言） | C、C++、Python、Rust、Verilog、MATLAB、CMake、Bash、PowerShell、LaTeX、Markdown | `tools/tech_stack.py` 的 `ROWS` |
| 技术栈第二行（嵌入式与硬件） | ST、TI、亚德诺、乐鑫、雅特力、Arduino、Keil、LVGL、Altium、Cadence、KiCad、EasyEDA、SolidWorks | 同上 |
| 技术栈第三行（软件与工具） | TS、JS、HTML、CSS、React、Tauri、Node.js、Vite、SQLite、Qt、Linux、Git | 同上 |
| 技术栈悬停说明 | 每个图标一句英文说明，例如 C — systems programming language | `ROWS` 里每一项的第三个字段；手机上没有悬停，看不到 |
| 统计卡片标题 | Alvin Li's GitHub Stats | 自动读取你 GitHub 资料里的名字 |

在 `README.md` 里搜 ✏️ 就能找到每一处可以改的地方。

## 打字动画和横幅的转义规则

这两个是图片服务的链接，GitHub 的图片代理不接受链接里直接出现 `×`、`·` 这类字符，写错会显示成裂图。

| 想写的字符 | 打字动画里写成 | 横幅里写成 |
|---|---|---|
| 空格 | `+` | `%20` |
| × | `%C3%97` | `%C3%97` |
| · | `%C2%B7` | `%C2%B7` |
| + | `%2B` | `%2B` |
| & | `%26` | `%26` |
| , | `%2C` | `%2C` |
| / | 直接写 | `%2F` |
| 换下一行 | `;` | 不适用 |

英文字母、数字和 `-` `.` 可以直接写。
