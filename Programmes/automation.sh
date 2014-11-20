./as Client1#1.2.3.4#TGS1 > tmp1
echo | cat tmp1
./decrypteur Client1 "$(< tmp1)" > tmp2
echo | cat tmp2
./tgs Client1#1.2.3.4#V1#"$(< tmp2)" > tmp3
echo | cat tmp3
./serveur Client1#1.2.3.4#V1#"$(< tmp3)" > tmp4
echo | cat tmp4

rm tmp*
