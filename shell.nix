{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell { nativeBuildInputs = with pkgs; [ atomicparsley youtube-dl ]; }
