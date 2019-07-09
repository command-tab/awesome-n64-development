## Community

* [N64brew](https://discord.gg/aU6Bkcc) - Nintendo 64 homebrew chat on Discord
* [Discord64](https://discord.gg/FrPyDtr) - Nintendo 64 emulation and homebrew chat on Discord
* [/r/N64Homebrew](https://www.reddit.com/r/N64Homebrew/) - The N64Homebrew subreddit

## Documentation

* [Ultra64](https://ultra64.ca/) - An absolute wealth of documentation including official Nintendo 64 development manuals, as well as SDK downloads and reference material
* [N64dev](http://n64dev.org/) - Useful N64 hacking links
* [NEC VR4300i CPU Manual @ N64dev](http://n64dev.org/p/U10504EJ7V0UMJ1.pdf) - The manual for the NEC VR4300i CPU used by the Nintendo 64
* [N64TEK](http://n64.icequake.net/mirror/www.jimb.de/Projects/N64TEK.htm) - Nintendo 64 technical information, registers, memory map, and instruction set
* [dragonminded N64DEV](https://dragonminded.com/n64dev/) - `libdragon` usage, Windows and Linux toolchains, and RCP documentation
* [N64 Uncompiled Source Code](http://shygoo.net/n64-uncompiled/) - Uncompiled source code and related material discovered in various Nintendo 64 ROM images
* [N64 ROM Formats](http://n64dev.org/romformats.html) - A short N64 ROM format quick reference sheet 
* [N64 ROM Formats Explained](https://www.reddit.com/r/emulation/comments/7hrvzp/the_three_different_n64_rom_formats_explained_for/?st=jn9t30t4&sh=1951de19) - Details the three commonly encountered Nintendo 64 ROM formats (use Big Endian/.z64)

## Toolchains

* [Official Nintendo 64 SDKs](https://ultra64.ca/resources/software/) - Official Nintendo 64 Software Development Kits for Windows and SGI IRIX
* [n64chain](https://github.com/tj90241/n64chain) - A Nintendo 64 development toolchain based on GCC that does not depend on any proprietary Nintendo library
* [modern-n64sdk](https://github.com/trhodeos/modern-n64sdk) - Describes how to get a modern build of GCC cross-compiling on a modern OS (Linux, Windows, macOS)
* [portable-n64-toolchain](https://github.com/Mr-Pnut/portable-n64-toolchain) - A Dockerized N64 toolchain based on modern-n64sdk

## Assemblers

* [ARM9/bass](https://github.com/ARM9/bass) - A fork of [bass](https://byuu.org/tool/bass/) which has been updated with N64 MIPS/RSP/RDP output
* [ARMIPS](https://github.com/Kingcom/armips) - An assembler for various ARM and MIPS platforms
* [Screwaround64](https://github.com/superjack111/screwaround64) - An interactive assembler for Nintendo 64

## Emulators

* [cen64](https://github.com/n64dev/cen64) - A [cycle-accurate](https://retrocomputing.stackexchange.com/questions/1191/what-exactly-is-a-cycle-accurate-emulator) Nintendo 64 emulator for Windows, Linux, and Mac. While currently not fast enough to play games at full speed, it aims perfect emulation by emulating the hardware inside of the console down to the register-transfer level.
* [Project64](https://www.pj64-emu.com) ([GitHub](https://github.com/project64/project64)) ([with Debugger](http://shygoo.net/pj64d/)) - An open source Nintendo 64 emulator for Windows and Android
* [1964](http://1964emu.emulation64.com) - An open-source Nintendo 64 emulator for Windows. No longer maintained.
* [mupen64](http://mupen64.emulation64.com) - An open-source, multi-platform Nintendo 64 emulator. No longer maintained.
* [mupen64plus](https://mupen64plus.org) ([GitHub](https://github.com/mupen64plus)) - A more recently updated fork of mupen64 for Linux, Mac OSX, FreeBSD, and Windows
* [Wii64](https://wiibrew.org/wiki/Wii64) - A port of mupen64 for Nintendo Wii and Gamecube. No longer maintained.
* [Mupen64-360](https://gbatemp.net/download/mupen64-360_v0-993_beta2.34126) - A port of Wii64 (and thus mupen64) to the Xbox 360. No longer maintained.
* Project Unreality - An early Nintendo 64 emulator for Windows. No longer maintained.
* [Nemu64](http://www.emulation64.com/files/info/202/nemu64.html/) - A closed-source Nintendo 64 emulator for Windows. No longer maintained.
* [UltraHLE](https://en.wikipedia.org/wiki/UltraHLE) - An early Nintendo 64 emulator for Windows. Though closed-source, [the source leaked in 2002](https://web.archive.org/web/20020812020546/http://www.emulation64.com/freeflow-page.html). No longer maintained.
* [Not64](https://github.com/extremscorner/not64) - A fork of Wii64
* [Surreal64](http://surreal64.sourceforge.net) and [Surreal64 CE](http://surreal64ce.wikidot.com) - A Nintendo 64 emulator for the original Xbox which includes ports of 1964, Project64, and UHLE. No longer maintained.
* [Sixtyforce](https://sixtyforce.com) - A closed-source Nintendo 64 emulator for Mac. No longer maintained.
* [TrueReality](https://sourceforge.net/projects/truereality/) - An open-source Nintendo 64 emulator. No longer maintained.

## Tools and Libraries

* [libdragon](https://github.com/DragonMinded/libdragon) - An open-source library for Nintendo 64 development
* [pseultra](https://github.com/pseudophpt/pseultra) - A collection of tools used to develop software for the Nintendo 64 that are distinct from the official SDK
* [libreultra](https://github.com/n64decomp/libreultra) - A decompilation of the Nintendo 64 standard SDK library, libultra
* [spicy](https://github.com/trhodeos/spicy) - An open-source version of the Nintendo 64 SDK's `mild.exe`. Assembles segments into an N64-compatible ROM.
* [makemask](https://github.com/trhodeos/makemask) - An open-source replacement of the Nintendo 64 SDK's `makemask.exe`. Adds a mask to a compiled ROM which pads the file and adds CIC information.
* [Online Disassembler](https://onlinedisassembler.com/odaweb/) - A lightweight, online service for when you don't have the time, resources, or requirements to use a heavier-weight alternative
* [Compiler Explorer](https://godbolt.org) - Explore how your C, C++, Rust, or other compiled language code ends up looking after compilation
* [mips_to_c](https://github.com/matt-kempster/mips_to_c) - An open-source MIPS decompiler, useful for understanding and reimplementing N64 games' behavior in C

## Development Hardware

* [64drive](http://64drive.retroactive.be/) - A Nintendo 64 flash cartridge with USB support targeted at developers
* [EverDrive-64 v3](https://krikzz.com/store/home/28-everdrive-64-v3.html) - A Nintendo 64 flash cartridge
* [UltraHDMI](http://ultrahdmi.retroactive.be/) (periodically in stock at [Game-Tech](https://www.game-tech.us/product/ultrahdmi/)) - A board that can be installed into the Nintendo 64 to capture the digital output of the RCP and send it out a Mini HDMI connector to a modern TV. Convenient for connecting a real console to a nearby monitor while viewing the best possible output signal.
* [UltraSave](http://64drive.retroactive.be/features.php#ultrasave) - A device that works with the 64drive to transfer saves from real cartridges
* [GameShark 3.0+](https://hackaday.com/2019/01/11/nintendo-64-homebrew-via-game-shark/) - A method of running homebrew on the Nintendo 64 via a GameShark

## Videos

* [Installing the Nintendo 64 Development Kit](https://www.youtube.com/watch?v=84wk0mZ8gfM) - How to install the Nintendo 64 Software Development Kit under Windows 2000 and 98SE. Also generally works under Windows XP.
* [Nintendo N64 Source Code Programming - A Basic Introduction](https://www.youtube.com/watch?v=d5YO2XMBvvk) - A basic introduction to Nintendo 64 development with with NuSystem and the official SDK
* [Building cen64 for Speed and Preservation](https://www.youtube.com/watch?v=lvr6-6U0ck8) - Making cen64 fast without compromising on accuracy
* [Reversing the Nintendo 64 CIC - REcon 2015](https://www.youtube.com/watch?v=HwEdqAb2l50) - Mike Ryan, marshallh, and John McMaster talk about reverse engineering and cloning a 20 year old copy protection chip (the N64 CIC)

## Assembly Programming

* [PeterLemon/N64](https://github.com/PeterLemon/N64) - Nintendo 64 bare metal MIPS assembly programming reference
* [Fraser N64](https://www.youtube.com/channel/UC3tcfSES8CB45DmTbHhUP1w) - YouTube channel featuring Nintendo 64 assembly programming
* [N64 Assembly Language Tutorial](https://sites.google.com/site/consoleprotocols/home/homebrew/n64-assembly-home) - Fraser's detailed Nintendo 64 assembly programming guide
* [N64-ASM-Tutorial](https://github.com/fraser125/N64-ASM-Tutorial) - The support files for N64 Assembly Language Tutorial
* [N64 ASM Tutorials](https://patater.com/gbaguy/n64asm.htm) - Nintendo 64 assembly language programming tutorials by Mike Huber (mirrored by Jaeden Amero)
* [UltraCIC](https://github.com/mikeryan/UltraCIC) - Not particularly homebrew development related, but is a useful reference as a clone of the Nintendo 64 CIC copy protection chip

## C Programming

* [N64 Homebrew Starter Guide](https://drive.google.com/drive/folders/1rOE2zYV2RPPx-2NHRGiGZ-RFx6w_6dAI) - Buu342's guide to creating an N64 game with the official Nintendo 64 SDK
* [Implementation of Sounds Using the Nintendo 64 Sound Tools](https://docs.google.com/document/d/1d1qKxMh3q_89w9N76xL9bXRqkXe1ylcDnAtg3cgu5s8) - Buu342's guide to implementing sound in your ROM with the Nintendo 64 Sound Tools
* [N64Squid Homebrew](https://n64squid.com/homebrew/n64-sdk) - Development walkthrough using the NuSystem library that's part of the official Nintendo 64 SDK

## Rust Programming

* [cargo-n64](https://github.com/rust-console/cargo-n64) - A `cargo` subcommand to build Nintendo 64 ROMs in Rust
* [n64toolchain](https://github.com/monocasa/n64toolchain) - Rust Implementation of Nintendo 64 ROM toolchain
* [rs64-rt](https://github.com/monocasa/rs64-rt) - Minimal Rust startup / runtime for Nintendo 64
* [rs64-periph](https://github.com/monocasa/rs64-periph) - Fairly raw N64 MMIO definitions
* [rs64-rom](https://github.com/monocasa/rs64-rom) - Rust library from manipulating Nintendo 64 ROM images
* [rs64romtool](https://github.com/monocasa/rs64romtool) - Tool for manipulating Nintendo 64 ROM images (depends on rs64-rom)
* [rrt0](https://github.com/rust-console/rrt0) - A simple cross-platform runtime / startup for Rust on embedded devices
