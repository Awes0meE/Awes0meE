<!--
  Awes0meE 个人主页 README
  ✏️ 标记的地方是可以改的文案。这种注释块在 GitHub 上不会显示。
  示波器上的文字改 tools/scope.py，技术栈（含鼠标悬停说明）改 tools/tech_stack.py，改完运行对应脚本重新生成。
-->

<!-- ✏️ 顶部横幅：text= 是大字，desc= 是小字。空格写 %20，× 写 %C3%97，· 写 %C2%B7，/ 写 %2F。深色、浅色、兜底三条要改成一样 -->
<a href="https://www.66ccff-labs.com">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:080808%2C55:11110F%2C100:FF7400&height=220&section=header&text=Alvin%20Li&fontColor=FAFAFA&fontSize=64&fontAlignY=36&animation=fadeIn&desc=Robotics%20%C3%97%20Full-stack%20%C2%B7%20iRidium%20Lab&descAlignY=58&descSize=18">
    <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:FFFFFF%2C60:DBEAFE%2C100:2563EB&height=220&section=header&text=Alvin%20Li&fontColor=1E3A8A&fontSize=64&fontAlignY=36&animation=fadeIn&desc=Robotics%20%C3%97%20Full-stack%20%C2%B7%20iRidium%20Lab&descAlignY=58&descSize=18">
    <img alt="Alvin Li · Robotics × Full-stack · iRidium Lab" src="https://capsule-render.vercel.app/api?type=waving&color=0:FFFFFF%2C60:DBEAFE%2C100:2563EB&height=220&section=header&text=Alvin%20Li&fontColor=1E3A8A&fontSize=64&fontAlignY=36&animation=fadeIn&desc=Robotics%20%C3%97%20Full-stack%20%C2%B7%20iRidium%20Lab&descAlignY=58&descSize=18" width="100%">
  </picture>
</a>

<p align="center">
  <a href="https://www.66ccff-labs.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="assets/brand/iridium-lockup-dark.png">
      <source media="(prefers-color-scheme: light)" srcset="assets/brand/iridium-lockup-light.png">
      <img alt="iRidium" src="assets/brand/iridium-lockup-light.png" height="120">
    </picture>
  </a>
</p>
<!--
  ✏️ 一直在变的那行蓝色英文字（打字动画）。只改 lines= 后面那一段：
     - 每一行之间用英文分号 ; 隔开
     - 空格写成 +
     - 特殊字符必须转义，不然 GitHub 会显示成裂图：
         × → %C3%97    · → %C2%B7    + → %2B    & → %26    # → %23    , → %2C
     - 纯英文字母、数字、- / . 可以直接写
  现在这 3 行是：
     Robotics × Full-stack engineer
     MCU · PCB · Control · Sensor Fusion
     Tauri + Rust + React desktop tools
  颜色改 color=（6 位十六进制，不带 #），速度改 pause=（每行停留毫秒）。
-->

<p align="center">
  <img alt="Robotics × Full-stack engineer · MCU · PCB · Control · Sensor Fusion · Tauri + Rust + React desktop tools" src="https://readme-typing-svg.demolab.com/?font=Barlow+Condensed&weight=600&size=26&pause=1200&color=3B8EEA&center=true&vCenter=true&width=720&height=44&lines=Robotics+%C3%97+Full-stack+engineer;MCU+%C2%B7+PCB+%C2%B7+Control+%C2%B7+Sensor+Fusion;Tauri+%2B+Rust+%2B+React+desktop+tools">
  <br>
  <!-- ✏️ 打字动画下面那行中文小字 -->
  <sub>机器人系统硬件 · 嵌入式 · 姿态控制 · 传感器融合 &nbsp;|&nbsp; 硬件为主，软件随行</sub>
</p>

<!-- ✏️ 两个徽章：badge/ 后面是「左边文字-右边文字-颜色」。文字里空格写 _，减号写 --，下划线写 __ -->
<p align="center">
  <a href="https://www.66ccff-labs.com"><img alt="iRidium Lab website" src="https://img.shields.io/badge/iRidium_Lab-my_website-66CCFF?style=for-the-badge&labelColor=080808"></a>
  <a href="https://www.linkedin.com/in/zhiyi-li-3a0821429/"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-Alvin_Li-0A66C2?style=for-the-badge&labelColor=080808"></a>
</p>

<!-- 示波器：图上文字改 tools/scope.py。改了通道名的话，下面 <img alt=…> 里的通道名也要手动改 -->

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/svg/scope-dark.svg">
    <source media="(prefers-color-scheme: light)" srcset="assets/svg/scope-light.svg">
    <img alt="Oscilloscope with three overlapping saddle waves on CH1 Hardware, CH2 Firmware and CH3 Software" src="assets/svg/scope-light.svg" width="100%">
  </picture>
</p>

## About

<!-- ✏️ 自我介绍 -->
Robotic-systems hardware and embedded engineer. I work from schematic and PCB layout through MCU firmware, and I write the desktop and web software my hardware needs.

## Hardware

<!-- ✏️ 每张卡片：<b> 里是标题，<sub> 里是说明。板子图片在 assets/boards/ -->
<table>
  <tr>
    <td align="center" width="33%" valign="top">
      <a href="https://www.66ccff-labs.com/work/gan-quadrotor-esc-fyp"><img alt="GaN quadrotor ESC board" src="assets/boards/gan-esc.webp" width="240"></a>
      <br><b>GaN Quadrotor ESC</b>
      <br><sub>GaN FETs + LMG1210 driver, 5 board spins</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <a href="https://www.66ccff-labs.com/work/ad831-active-mixer"><img alt="AD831 active mixer board" src="assets/boards/ad831.webp" width="240"></a>
      <br><b>AD831 Active Mixer</b>
      <br><sub>120 MHz RF → 10.7 MHz IF, 4 revisions</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <a href="https://www.66ccff-labs.com/work/claude-chime-hardware-power-board"><img alt="Claude Chime power board, assembled" src="assets/boards/chime.webp" width="240"></a>
      <br><b>Claude Chime Power Board</b>
      <br><sub>ESP32 power board for Accele AI, 28 × 27 mm</sub>
    </td>
  </tr>
  <tr></tr>
  <tr>
    <td align="center" width="33%" valign="top">
      <a href="https://www.66ccff-labs.com/work/juanyun-thermal-hardware"><img alt="Cirro cooling controller main board" src="assets/boards/cirro.webp" width="240"></a>
      <br><b>Cirro Cooling Controllers</b>
      <br><sub>STM32 boards for phase-change cooling</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <a href="https://www.66ccff-labs.com/work/course-tool-boards"><img alt="12 V / 5 V / 3.3 V power supply board" src="assets/boards/tool-boards.webp" width="240"></a>
      <br><b>Course Project Tool Boards</b>
      <br><sub>Buck, USB PD multi-rail, charge-and-boost</sub>
    </td>
    <td align="center" width="33%" valign="top">
      <!-- 这张还没有作品集页面，先不加链接；套在 picture 里是为了让 GitHub 不把图片变成可点开的大图 -->
      <picture><img alt="ASRPRO voice module and OLED controller board" src="assets/boards/voice-light.webp" width="240"></picture>
      <br><b>Wireless Voice-Controlled Light</b>
      <br><sub>ASRPRO voice recognition + OLED controller</sub>
    </td>
  </tr>
</table>

<p align="right"><a href="https://www.66ccff-labs.com/work">→ all projects on 66ccff-labs.com/work</a></p>

## Tech stack

<!-- ✏️ 技术栈三行（语言 / 嵌入式与硬件 / 软件与工具）和鼠标悬停时浮出的说明，都在 tools/tech_stack.py 的 ROWS 里改，改完运行 python tools/tech_stack.py -->
<!-- tech-stack:start：这一段由 tools/tech_stack.py 自动生成，不要手改；改图标或悬停说明请改那个脚本里的 ROWS -->
<p align="center">
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/c-dark.svg"><img src="assets/svg/stack/c-light.svg" alt="C" title="C — systems programming language"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/cpp-dark.svg"><img src="assets/svg/stack/cpp-light.svg" alt="C++" title="C++ — systems programming language"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/python-dark.svg"><img src="assets/svg/stack/python-light.svg" alt="Python" title="Python — scripting and data processing"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/rust-dark.svg"><img src="assets/svg/stack/rust-light.svg" alt="Rust" title="Rust — memory-safe systems language"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/verilog-dark.svg"><img src="assets/svg/stack/verilog-light.svg" alt="Verilog" title="Verilog — hardware description language"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/matlab-dark.svg"><img src="assets/svg/stack/matlab-light.svg" alt="MATLAB" title="MATLAB — numerical computing and simulation"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/cmake-dark.svg"><img src="assets/svg/stack/cmake-light.svg" alt="CMake" title="CMake — cross-platform C/C++ build system"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/bash-dark.svg"><img src="assets/svg/stack/bash-light.svg" alt="Bash" title="Bash — Unix shell scripting"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/powershell-dark.svg"><img src="assets/svg/stack/powershell-light.svg" alt="PowerShell" title="PowerShell — Windows shell scripting"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/latex-dark.svg"><img src="assets/svg/stack/latex-light.svg" alt="LaTeX" title="LaTeX — technical document typesetting"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/md-dark.svg"><img src="assets/svg/stack/md-light.svg" alt="Markdown" title="Markdown — lightweight markup language"></picture><br>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/stmicroelectronics-blue-white-dark.svg"><img src="assets/svg/stack/stmicroelectronics-blue-white-light.svg" alt="STMicroelectronics" title="STMicroelectronics — STM32 microcontrollers"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/texas-instruments-symbol-transparent-dark.svg"><img src="assets/svg/stack/texas-instruments-symbol-transparent-light.svg" alt="Texas Instruments" title="Texas Instruments — MSPM0 microcontrollers"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/adi-dark.svg"><img src="assets/svg/stack/adi-light.svg" alt="Analog Devices" title="Analog Devices — analog, mixed-signal and RF ICs"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/espressif-symbol-dark.svg"><img src="assets/svg/stack/espressif-symbol-light.svg" alt="Espressif" title="Espressif — ESP32 Wi-Fi / Bluetooth SoCs"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/artery-wordmark-dark.svg"><img src="assets/svg/stack/artery-wordmark-light.svg" alt="Artery" title="Artery — AT32 microcontrollers"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/arduino-dark.svg"><img src="assets/svg/stack/arduino-light.svg" alt="Arduino" title="Arduino — open-source microcontroller platform"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/keil-uvision-dark.svg"><img src="assets/svg/stack/keil-uvision-light.svg" alt="Keil µVision" title="Keil µVision — embedded C IDE for MCUs"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/lvgl-dark.svg"><img src="assets/svg/stack/lvgl-light.svg" alt="LVGL" title="LVGL — embedded graphics library"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/altium-designer-dark.svg"><img src="assets/svg/stack/altium-designer-light.svg" alt="Altium Designer" title="Altium Designer — schematic and PCB design"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/cadence-pcb-editor-clean-dark.svg"><img src="assets/svg/stack/cadence-pcb-editor-clean-light.svg" alt="Cadence Allegro" title="Cadence Allegro — PCB design"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/kicad-logo-dark.svg"><img src="assets/svg/stack/kicad-logo-light.svg" alt="KiCad" title="KiCad — open-source schematic and PCB design"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/easyeda-dark.svg"><img src="assets/svg/stack/easyeda-light.svg" alt="EasyEDA" title="EasyEDA — online schematic and PCB design"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/solidworks-user-drawn-transparent-dark.svg"><img src="assets/svg/stack/solidworks-user-drawn-transparent-light.svg" alt="SOLIDWORKS" title="SOLIDWORKS — 3D mechanical CAD"></picture><br>
<picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/ts-dark.svg"><img src="assets/svg/stack/ts-light.svg" alt="TypeScript" title="TypeScript — typed JavaScript"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/js-dark.svg"><img src="assets/svg/stack/js-light.svg" alt="JavaScript" title="JavaScript — language of the web"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/html-dark.svg"><img src="assets/svg/stack/html-light.svg" alt="HTML" title="HTML — web page markup"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/css-dark.svg"><img src="assets/svg/stack/css-light.svg" alt="CSS" title="CSS — web page styling"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/react-dark.svg"><img src="assets/svg/stack/react-light.svg" alt="React" title="React — UI library"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/tauri-dark.svg"><img src="assets/svg/stack/tauri-light.svg" alt="Tauri" title="Tauri — Rust-based desktop app framework"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/nodejs-dark.svg"><img src="assets/svg/stack/nodejs-light.svg" alt="Node.js" title="Node.js — JavaScript runtime"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/vite-dark.svg"><img src="assets/svg/stack/vite-light.svg" alt="Vite" title="Vite — front-end build tool"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/sqlite-dark.svg"><img src="assets/svg/stack/sqlite-light.svg" alt="SQLite" title="SQLite — embedded database"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/qt-dark.svg"><img src="assets/svg/stack/qt-light.svg" alt="Qt" title="Qt — cross-platform C++ UI framework"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/linux-dark.svg"><img src="assets/svg/stack/linux-light.svg" alt="Linux" title="Linux — open-source operating system"></picture><picture><source media="(prefers-color-scheme: dark)" srcset="assets/svg/stack/git-dark.svg"><img src="assets/svg/stack/git-light.svg" alt="Git" title="Git — version control"></picture>
</p>
<!-- tech-stack:end -->

## GitHub

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://github-stats-extended.vercel.app/api?username=Awes0meE&hide_rank=true&show_icons=true&hide_border=true&bg_color=11110F&title_color=FF7400&icon_color=66CCFF&text_color=FAFAFA&ring_color=66CCFF&hide=contribs&include_all_commits=false">
    <source media="(prefers-color-scheme: light)" srcset="https://github-stats-extended.vercel.app/api?username=Awes0meE&hide_rank=true&show_icons=true&bg_color=FFFFFF&title_color=2563EB&icon_color=38BDF8&text_color=1E3A8A&ring_color=2563EB&border_color=E5E7EB&hide=contribs&include_all_commits=false">
    <img alt="GitHub stats" src="https://github-stats-extended.vercel.app/api?username=Awes0meE&hide_rank=true&show_icons=true&bg_color=FFFFFF&title_color=2563EB&icon_color=38BDF8&text_color=1E3A8A&ring_color=2563EB&border_color=E5E7EB&hide=contribs&include_all_commits=false" height="165">
  </picture>
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com/?user=Awes0meE&hide_border=true&background=11110F&ring=66CCFF&fire=FF7400&currStreakNum=FAFAFA&sideNums=FAFAFA&currStreakLabel=66CCFF&sideLabels=FAFAFA&dates=9A9A9A&stroke=333333">
    <source media="(prefers-color-scheme: light)" srcset="https://streak-stats.demolab.com/?user=Awes0meE&background=FFFFFF&ring=2563EB&fire=FF7400&currStreakNum=1E3A8A&sideNums=1E3A8A&currStreakLabel=2563EB&sideLabels=1E3A8A&dates=64748B&stroke=E5E7EB&border=E5E7EB">
    <img alt="GitHub streak" src="https://streak-stats.demolab.com/?user=Awes0meE&background=FFFFFF&ring=2563EB&fire=FF7400&currStreakNum=1E3A8A&sideNums=1E3A8A&currStreakLabel=2563EB&sideLabels=1E3A8A&dates=64748B&stroke=E5E7EB&border=E5E7EB" height="165">
  </picture>
</p>

<!-- 贪吃蛇：.github/workflows/snake.yml 每天和每次推送到 main 时重新生成到 output 分支。仓库 60 天没有动静时 GitHub 会暂停定时任务，到 Actions 页面重新启用即可 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Awes0meE/Awes0meE/output/github-snake-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Awes0meE/Awes0meE/output/github-snake.svg">
  <img alt="contribution snake" src="https://raw.githubusercontent.com/Awes0meE/Awes0meE/output/github-snake.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:080808%2C55:11110F%2C100:FF7400&height=120&section=footer">
  <source media="(prefers-color-scheme: light)" srcset="https://capsule-render.vercel.app/api?type=waving&color=0:FFFFFF%2C60:DBEAFE%2C100:2563EB&height=120&section=footer">
  <img alt="" src="https://capsule-render.vercel.app/api?type=waving&color=0:FFFFFF%2C60:DBEAFE%2C100:2563EB&height=120&section=footer" width="100%">
</picture>
