#!/usr/bin/env bash
echo ""
echo "Appel de AS..."
./as Client1#1.2.3.4#TGS1 > tmp1
echo "Retour de AS:"
echo | cat tmp1
echo ""
echo "Appel de decrypteur..."
./decrypteur Client1 "$(< tmp1)" > tmp2
echo "Retour de decrypteur:"
echo | cat tmp2
echo ""
echo "Appel de TGS..."
./tgs Client1#1.2.3.4#V1#"$(< tmp2)" > tmp3
echo "Retour de tgs:"
echo | cat tmp3
echo ""
echo "Appel de Serveur..."
./serveur Client1#1.2.3.4#V1#"$(< tmp3)" > tmp4
echo "Retour de Serveur:"
echo | cat tmp4
echo ""

rm tmp*
