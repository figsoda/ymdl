{
  inputs = {
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: {
      devShell = with nixpkgs.legacyPackages.${system};
        mkShell { buildInputs = [ atomicparsley python3 youtube-dl ]; };
    });
}
