const readline = require('readline');

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

rl.question("", (data) => {
    var n = parseInt(data);
    var trie = {};
    rl.on("line", (s) => {
        var node = trie;
        
        for (var i = 0; i < s.length; i ++) {
            var c = s[i];
            if (node[c] === undefined) {
                node[c] = {val: 0};
            }
            node[c].val ++;
            node = node[c];
        }
        console.log(node.val - 1);
    });
});
