$out_dir = 'out';
# Copy PDF back to source directory after build
END { system("cp $out_dir/*.pdf . 2>/dev/null") if defined $out_dir; }
