{
  inputs.flake-utils.url = "github:numtide/flake-utils";

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system: {
      devShell = with nixpkgs.legacyPackages.${system};
        mkShell {
          buildInputs =
            [ (python3.withPackages (ps: [ ps.pytaglib ])) youtube-dl ];
        };
    });
}
