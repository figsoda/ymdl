with import <nixpkgs> { };

mkShell { buildInputs = [ atomicparsley youtube-dl ]; }
