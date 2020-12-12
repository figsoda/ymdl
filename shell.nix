with import <nixpkgs> { };

mkShell { buildInputs = [ atomicparsley python3 youtube-dl ]; }
