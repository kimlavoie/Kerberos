#!/usr/bin/env bash
./as Client1#1.2.3.4#TGS1 > tmp1
echo ""
echo "Appel de AS..."
echo "Retour de AS:"
echo | cat tmp1
echo ""
./decrypteur Client1 "$(< tmp1)" > tmp2
echo "Appel de decrypteur..."
echo "Retour de decrypteur:"
echo | cat tmp2
echo ""
./tgs Client1#1.2.3.4#V1#"$(< tmp2)" > tmp3
echo "Appel de TGS..."
echo "Retour de tgs:"
echo | cat tmp3
echo ""
./serveur Client1#1.2.3.4#V1#"$(< tmp3)" > tmp4
echo "Appel de Serveur..."
echo "Retour de Serveur:"
echo | cat tmp4
echo ""

rm tmp*
