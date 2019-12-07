# Awesome N64 Development

A curated list of Nintendo 64 development resources including toolchains, documentation, emulators, and more

## Contents

* [Community](#community)
* [Documentation](#documentation)
* [Toolchains](#toolchains)
* [Assemblers](#assemblers)
* [Emulators](#emulators)
* [Development Hardware](#development-hardware)
* [Tools and Libraries](#tools-and-libraries)
    * [Development Cartridge Loaders](#development-cartridge-loaders)
    * [Asset Conversion and Viewing](#asset-conversion-and-viewing)
    * [Audio Playback and Editing](#audio-playback-and-editing)
    * [Debugging](#debugging)
    * [ROM Manipulation](#rom-manipulation)
    * [Development Libraries](#development-libraries)
    * [Reverse Engineering](#reverse-engineering)
* [Videos](#videos)
* [Programming](#programming)
    * [Assembly](#assembly)
    * [C](#c)
    * [Rust](#rust)

## Community

* [N64brew](https://discord.gg/aU6Bkcc) - Nintendo 64 homebrew chat on Discord
* [Discord64](https://discord.gg/FrPyDtr) - Nintendo 64 emulation and homebrew chat on Discord
* [`#n64dev` on EFnet](http://chat.efnet.org/?channels=n64dev) - Nintendo 64 development IRC channel on EFnet
* [/r/N64Homebrew](https://www.reddit.com/r/N64Homebrew/) - The N64Homebrew subreddit

## Documentation

* [Ultra64](https://ultra64.ca/) - An absolute wealth of documentation including official Nintendo 64 development manuals, as well as SDK downloads and reference material
* [Nintendo 64 Architecture](https://copetti.org/projects/consoles/nintendo-64/) - An overview of the Nintendo 64 console architecture
* [N64dev](http://n64dev.org/) - Useful N64 hacking links
* [NEC VR4300i CPU Manual @ N64dev](http://n64dev.org/p/U10504EJ7V0UMJ1.pdf) - The manual for the NEC VR4300i CPU used by the Nintendo 64
* [N64TEK](http://n64.icequake.net/mirror/www.jimb.de/Projects/N64TEK.htm) - Nintendo 64 technical information, registers, memory map, and instruction set
* [dragonminded N64DEV](https://dragonminded.com/n64dev/) - `libdragon` usage, Windows and Linux toolchains, and RCP documentation
* [N64 ROM Formats](http://n64dev.org/romformats.html) - A short N64 ROM format quick reference sheet 
* [N64 ROM Formats Explained](https://www.reddit.com/r/emulation/comments/7hrvzp/the_three_different_n64_rom_formats_explained_for/?st=jn9t30t4&sh=1951de19) - Details the three commonly encountered Nintendo 64 ROM formats (use Big Endian/.z64)
* [Accessory Reference](http://github.com/joeldipops/TransferBoy/blob/master/docs/TransferPakReference.md) - Guide on how to communicate with the Transfer Pak and Rumble Pak
* [Hack64](https://hack64.net/wiki/doku.php?id=nintendo_64) - A variety of documentation on RCP data structures, compression, assembly, and more
* [Encryption 64](http://en64.shoutwiki.com/wiki/Main_Page) - A collection of documentation on MIPS assembly, GameShark code structure, and layout of individual titles
* [64dd wiki](https://github.com/LuigiBlood/64dd/wiki) - Documentation on 64DD hardware, disks, and related catridges

## Toolchains

* [Official Nintendo 64 SDKs](https://ultra64.ca/resources/software/) - Official Nintendo 64 Software Development Kits for Windows and SGI IRIX
* [N64 SDK Easy Install](https://mega.nz/#!oT4hlS7A!OS_8zDMezzjXoQiil9SJd1D8kAFbEkYqJKdsj2B8hkk) - A ISO image made by AlphaTango and CrashOveride to allow for a easier way to install the SDK. Confirmed working on Windows 98-XP
* [n64chain](https://github.com/tj90241/n64chain) - A Nintendo 64 development toolchain based on GCC that does not depend on any proprietary Nintendo library
* [modern-n64sdk](https://github.com/trhodeos/modern-n64sdk) - Describes how to get a modern build of GCC cross-compiling on a modern OS (Linux, Windows, macOS)
* [portable-n64-toolchain](https://github.com/Mr-Pnut/portable-n64-toolchain) - A Dockerized N64 toolchain based on modern-n64sdk
* [libdragon-docker](https://github.com/anacierdem/libdragon-docker) - Dockerized toolchain based on [libdragon](https://github.com/DragonMinded/libdragon).

## Assemblers

* [ARM9/bass](https://github.com/ARM9/bass) - A fork of [bass](https://byuu.org/tool/bass/) which has been updated with N64 MIPS/RSP/RDP output
* [ARMIPS](https://github.com/Kingcom/armips) - An assembler for various ARM and MIPS platforms
* [Screwaround64](https://github.com/superjack111/screwaround64) - An interactive assembler for Nintendo 64

## Emulators

* [cen64](https://github.com/n64dev/cen64) - A [cycle-accurate](https://retrocomputing.stackexchange.com/questions/1191/what-exactly-is-a-cycle-accurate-emulator) Nintendo 64 emulator for Windows, Linux, and Mac. While currently not fast enough to play games at full speed, it aims for perfect emulation by emulating the hardware inside of the console down to the register-transfer level.
* [cor64](https://github.com/bryanperris/cor64) - An in-progress Nintendo 64 emulator written in C#
* [Project64](https://www.pj64-emu.com) ([GitHub](https://github.com/project64/project64)) ([with Debugger](http://shygoo.net/pj64d/)) - An open source Nintendo 64 emulator for Windows and Android
* [1964](http://1964emu.emulation64.com) - An open-source Nintendo 64 emulator for Windows. No longer maintained.
* [mupen64](http://mupen64.emulation64.com) - An open-source, multi-platform Nintendo 64 emulator. No longer maintained.
* [mupen64plus](https://mupen64plus.org) ([GitHub](https://github.com/mupen64plus)) - A more recently updated fork of mupen64 for Linux, Mac OSX, FreeBSD, and Windows
* [Mupen64+ Reverser Edition](https://www.retroreversing.com/mupen64RE) - A fork of the Mupen64+ Nintendo 64 emulator tailored for reverse engineering
* [Wii64](https://wiibrew.org/wiki/Wii64) - A port of mupen64 for Nintendo Wii and Gamecube. No longer maintained.
* [Mupen64-360](https://gbatemp.net/download/mupen64-360_v0-993_beta2.34126) - A port of Wii64 (and thus mupen64) to the Xbox 360. No longer maintained.
* Project Unreality - An early Nintendo 64 emulator for Windows. No longer maintained.
* [Nemu64](http://www.emulation64.com/files/info/202/nemu64.html/) - A closed-source Nintendo 64 emulator for Windows. No longer maintained.
* [UltraHLE](https://en.wikipedia.org/wiki/UltraHLE) - An early Nintendo 64 emulator for Windows. Though closed-source, [the source leaked in 2002](https://web.archive.org/web/20020812020546/http://www.emulation64.com/freeflow-page.html). No longer maintained.
* [Not64](https://github.com/extremscorner/not64) - A fork of Wii64
* [Surreal64](http://surreal64.sourceforge.net) and [Surreal64 CE](http://surreal64ce.wikidot.com) - A Nintendo 64 emulator for the original Xbox which includes ports of 1964, Project64, and UHLE. No longer maintained.
* [Sixtyforce](https://sixtyforce.com) - A closed-source Nintendo 64 emulator for Mac
* [TrueReality](https://sourceforge.net/projects/truereality/) - An open-source Nintendo 64 emulator. No longer maintained.

## Development Hardware

* [64drive](http://64drive.retroactive.be/) - A Nintendo 64 flash cartridge with USB support targeted at developers
* [EverDrive-64 x7](https://krikzz.com/store/home/55-everdrive-64-x7.html) - A Nintendo 64 flash cartridge
* [UltraHDMI](http://ultrahdmi.retroactive.be/) (periodically in stock at [Game-Tech](https://www.game-tech.us/product/ultrahdmi/)) - A board that can be installed into the Nintendo 64 to capture the digital output of the RCP and send it out a Mini HDMI connector to a modern TV. Convenient for connecting a real console to a nearby monitor while viewing the best possible output signal.
* [UltraSave](http://64drive.retroactive.be/features.php#ultrasave) - A device that works with the 64drive to transfer saves from real cartridges
* [GameShark 3.0+](https://hackaday.com/2019/01/11/nintendo-64-homebrew-via-game-shark/) - A method of running homebrew on the Nintendo 64 via a GameShark

## Tools and Libraries

### Development Cartridge Loaders

* [64drive-usb-linux](https://github.com/RenaKunisaki/64drive-usb-linux/) - A Linux tool to upload to/download from a 64drive development cartridge over USB
* [g64drive](https://github.com/rasky/g64drive) - Linux/Mac tool for operating a 64drive development cartridge
* [ed64](https://github.com/anacierdem/ed64) - Tools to develop on an EverDrive-64 cartridge

### Asset Conversion and Viewing

* [64Drive Viewer](https://www.youtube.com/watch?v=yUX1Vga6amg) - Preview textures, images, sounds, and 3D models on the Nintendo 64 with a 64drive over USB
* [Blen64](https://github.com/GCaldL/Blen64) - Blender scripts to export meshes to draw lists as header files
* [objn64](https://github.com/n64dev/objn64) - Wavefront `.obj` model converter that generates optimized Nintendo 64 displaylists for compilation with libultra
* [Obj2N64DL](https://github.com/pseudophpt/Obj2N64DL) - Another Wavefront `.obj` to displaylist converter
* [n64CIconverter](https://github.com/darklink623/n64CIconverter) - Converts standard image formats to Nintendo 64's CI format
* [N64GFXCookie](https://github.com/LuigiBlood/N64GFXCookie) - Nintendo 64 CI8 format graphics viewer/editor
* [Texture64](https://github.com/queueRAM/Texture64) - Nintendo 64 texture ripper and editor with support for multiple formats
* [N64-SoundTester](https://github.com/buu342/N64-SoundTester) - A ROM that allows you to test out N64 Sound Tools sample banks and tune them directly on your console or emulator, avoiding lengthy turnaround times
* [leotools](https://github.com/jkbenaim/leotools) - Tools for working with 64DD images and related files

### Audio Playback and Editing

* [N64-Tools](https://github.com/jombo23/N64-Tools/tree/master/N64%20Midi%20Tool) - A tool to extract and import audio from many games that make use of the MIDI format
* [libmad-n64](https://github.com/parasyte/libmad-n64) - [libmad](https://www.underbit.com/products/mad/) with MIPS patches, for MPEG audio playback
* [seq64](https://github.com/sauraen/seq64) - A full-featured editor for sequenced music in first-party Nintendo 64 games

### Debugging

* [Project64 EmuScripts](https://github.com/LuigiBlood/EmuScripts/tree/master/N64/Project64) - Scripts for debugging under Project64 emulation

### ROM Manipulation

* [spicy](https://github.com/trhodeos/spicy) - An open-source replacement of the Nintendo 64 SDK's `mild.exe` (referenced by `$(MAKEROM)` in many Makefiles). Packs object files into an N64-compatible ROM.
* [makemask](https://github.com/trhodeos/makemask) - An open-source replacement of the Nintendo 64 SDK's `makemask.exe`. Adds a mask to a compiled ROM which pads the file to fill the entire cartridge space, adds a CIC version, and adds informational headers to the file. Typically run immediately after `mild.exe`. More on this tool at [N64Squid](https://n64squid.com/homebrew/n64-sdk/software/mipse-ultra-gcc/makemask/).
* [Tool N64](https://www.zophar.net/utilities/n64aud/tool-n64.html) - A tool to display ROM information and perform byte reordering

### Development Libraries

* [libdragon](https://github.com/DragonMinded/libdragon) - An open-source library for Nintendo 64 development
* [pseultra](https://github.com/pseudophpt/pseultra) - A collection of tools used to develop software for the Nintendo 64 that are distinct from the official SDK
* [libreultra](https://github.com/n64decomp/libreultra) - A decompilation of the Nintendo 64 standard SDK library, `libultra`

### Reverse Engineering

* [N64LoaderWV](https://github.com/zeroKilo/N64LoaderWV) - Nintendo 64 ROM loader for the [Ghidra](https://github.com/NationalSecurityAgency/ghidra) reverse engineering tool
* [n64decomp](https://github.com/n64decomp/) - Nintendo 64 decompilation projects, including Super Mario 64 and The Legend of Zelda: Ocarina of Time (Master Quest) (OOT is WIP and not public yet)
* [N64 Uncompiled Source Code](http://shygoo.net/n64-uncompiled/) - Uncompiled source code and related material discovered in various Nintendo 64 ROM images
* [RI Probe](https://www.romhacking.net/homebrew/102/) - A ROM that dumps RDRAM values onscreen for debugging and exploring
* [n64sym](https://github.com/shygoo/n64sym) - Scans a RAM dump for symbols from a given library or object file
* [Online Disassembler](https://onlinedisassembler.com/odaweb/) - A lightweight, online service for when you don't have the time, resources, or requirements to use a heavier-weight alternative
* [Compiler Explorer](https://godbolt.org) - Explore how your C, C++, Rust, or other compiled language code ends up looking after compilation
* [mips_to_c](https://github.com/matt-kempster/mips_to_c) - An open-source MIPS decompiler, useful for understanding and reimplementing N64 games' behavior in C
* [GEDecompressor](https://github.com/jombo23/N64-Tools/tree/master/GEDecompressor) - Decompressor for a wide variety of compression formats used across Nintendo 64 titles
* [asm-differ](https://github.com/simonlindholm/asm-differ) - A `diff` script for MIPS assembly
* [decomp-permuter](https://github.com/simonlindholm/decomp-permuter) - A tool to randomly permute C files to better match a target binary

## Videos

* [Installing the Nintendo 64 Development Kit](https://www.youtube.com/watch?v=84wk0mZ8gfM) - How to install the Nintendo 64 Software Development Kit under Windows 2000 and 98SE and build sample code. Also generally works under Windows XP.
* [Nintendo N64 Source Code Programming - A Basic Introduction](https://www.youtube.com/watch?v=d5YO2XMBvvk) - A basic introduction to Nintendo 64 development with with NuSystem and the official SDK
* [Building cen64 for Speed and Preservation](https://www.youtube.com/watch?v=lvr6-6U0ck8) - Making cen64 fast without compromising on accuracy
* [Reversing the Nintendo 64 CIC - REcon 2015](https://www.youtube.com/watch?v=HwEdqAb2l50) - Mike Ryan, marshallh, and John McMaster talk about reverse engineering and cloning a 20 year old copy protection chip (the N64 CIC)

## Programming

### Assembly

* [PeterLemon/N64](https://github.com/PeterLemon/N64) - Nintendo 64 bare metal MIPS assembly programming reference
* [Fraser N64](https://www.youtube.com/channel/UC3tcfSES8CB45DmTbHhUP1w) - YouTube channel featuring Nintendo 64 assembly programming
* [N64 Assembly Language Tutorial](https://sites.google.com/site/consoleprotocols/home/homebrew/n64-assembly-home) - Fraser's detailed Nintendo 64 assembly programming guide
* [N64-ASM-Tutorial](https://github.com/fraser125/N64-ASM-Tutorial) - The support files for N64 Assembly Language Tutorial
* [N64 ASM Tutorials](https://patater.com/gbaguy/n64asm.htm) - Nintendo 64 assembly language programming tutorials by Mike Huber (mirrored by Jaeden Amero)
* [UltraCIC](https://github.com/mikeryan/UltraCIC) - Not particularly homebrew development related, but is a useful reference as a clone of the Nintendo 64 CIC copy protection chip

### C

* [N64 Homebrew Starter Guide](https://drive.google.com/drive/folders/1rOE2zYV2RPPx-2NHRGiGZ-RFx6w_6dAI) - Buu342's guide to creating an N64 game with the official Nintendo 64 SDK
* [Implementation of Sounds Using the Nintendo 64 Sound Tools](https://docs.google.com/document/d/1d1qKxMh3q_89w9N76xL9bXRqkXe1ylcDnAtg3cgu5s8) - Buu342's guide to implementing sound in your ROM with the Nintendo 64 Sound Tools
* [N64Squid Homebrew](https://n64squid.com/homebrew/n64-sdk) - Development walkthrough using the NuSystem library that's part of the official Nintendo 64 SDK

### Rust

* [cargo-n64](https://github.com/rust-console/cargo-n64) - A `cargo` subcommand to build Nintendo 64 ROMs in Rust
* [n64toolchain](https://github.com/monocasa/n64toolchain) - Rust Implementation of Nintendo 64 ROM toolchain
* [rs64-rt](https://github.com/monocasa/rs64-rt) - Minimal Rust startup / runtime for Nintendo 64
* [rs64-periph](https://github.com/monocasa/rs64-periph) - Fairly raw N64 MMIO definitions
* [rs64-rom](https://github.com/monocasa/rs64-rom) - Rust library from manipulating Nintendo 64 ROM images
* [rs64romtool](https://github.com/monocasa/rs64romtool) - Tool for manipulating Nintendo 64 ROM images (depends on rs64-rom)
* [rrt0](https://github.com/rust-console/rrt0) - A simple cross-platform runtime / startup for Rust on embedded devices
* [n64rom-rs](https://github.com/saneki/n64rom-rs) - A library and toolkit for working with Nintendo 64 ROM files
