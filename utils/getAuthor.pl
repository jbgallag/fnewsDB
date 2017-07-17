

open(FILE, "$ARGV[0]");
while(<FILE>) {
    $_ =~ tr/\n//d;
    @data = split(/\t/ , $_);
    @name = split(/\s/, $data[1]);
    for($i=0; $i<=$#name; $i++) {
       $revName = join' ',$revName,$name[$#name-$i];
    }
    $revName =~ s/^\s+//g;
    #print "$revName\n";
    $NAMES{$revName} = $NAMES{$revName} + 1;
    $revName = '';
}

@nkeys = keys %NAMES;

foreach $key (@nkeys) {
   print "$key\n";
}
