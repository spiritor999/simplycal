#!/usr/bin/env python3
"""
修复 game.html 中的讲解逻辑
"""
import re

# 读取文件
with open('game.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 新的讲解函数
new_explanation_code = '''            getExplanation: function(question, answer, method) {
                // 解析题目：提取所有数字和运算符
                const nums = question.split(/[\\+\\-\\×\\÷]/).map(s => s.trim());
                const operators = question.match(/[\\+\\-\\×\\÷]/g) || [];
                const numbers = nums.map(n => parseInt(n));

                // 判断题目类型（两个数或三个数）
                const isThreeNumber = numbers.length >= 3;

                if (isThreeNumber) {
                    // 三个数以上的题目
                    return this.getThreeNumberExplanation(question, answer, method, numbers, operators);
                } else {
                    // 两个数的题目
                    return this.getTwoNumberExplanation(question, answer, method, numbers, operators);
                }
            },

            // 两个数题目的讲解
            getTwoNumberExplanation: function(question, answer, method, numbers, operators) {
                const num1 = numbers[0];
                const num2 = numbers[1];
                const operator = operators[0];

                switch(method) {
                    case '凑十法':
                        const comp = 10 - num1;
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>使用凑十法：</strong><br>
                        想想看，怎么才能凑成10呢？<br>
                        ${num1} + ${num2} = ${num1} + (${comp} + ${num2 - comp})<br>
                        = (${num1} + ${comp}) + ${num2 - comp}<br>
                        = 10 + ${num2 - comp}<br>
                        = <strong>${answer}</strong>`;

                    case '破十法':
                        const sub = num1 - 10;
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>使用破十法：</strong><br>
                        先把10减掉，剩下的再处理<br>
                        ${num1} - ${num2} = (10 - ${num2}) + ${sub}<br>
                        = ${10 - num2} + ${sub}<br>
                        = <strong>${answer}</strong>`;

                    case '加法交换律':
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>使用加法交换律：</strong><br>
                        交换加数的位置，和不变<br>
                        ${num1} + ${num2} = ${num2} + ${num1}<br>
                        = <strong>${answer}</strong>`;

                    case '加法结合律':
                        const compAdd = Math.ceil(num1 / 10) * 10 - num1;
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>使用加法结合律：</strong><br>
                        凑整十数更容易计算<br>
                        ${num1} + ${num2}<br>
                        = (${num1} + ${compAdd}) + (${num2} - ${compAdd})<br>
                        = ${num1 + compAdd} + ${num2 - compAdd}<br>
                        = <strong>${answer}</strong>`;

                    case '凑整法':
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>使用凑整法：</strong><br>
                        把数凑成整十数更容易计算<br>
                        ${question}<br>
                        = <strong>${answer}</strong>`;

                    default:
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>直接计算：</strong><br>
                        ${question}<br>
                        = <strong>${answer}</strong>`;
                }
            },

            // 三个数题目的讲解
            getThreeNumberExplanation: function(question, answer, method, numbers, operators) {
                // 生成逐步计算的讲解
                let steps = [question];

                let currentResult = numbers[0];
                let currentExpression = `${numbers[0]}`;

                for (let i = 0; i < operators.length; i++) {
                    const operator = operators[i];
                    const nextNum = numbers[i + 1];

                    if (operator === '+') {
                        currentResult += nextNum;
                    } else {
                        currentResult -= nextNum;
                    }

                    currentExpression += ` ${operator} ${nextNum}`;
                    steps.push(currentExpression);
                }

                // 根据方法生成讲解
                switch(method) {
                    case '凑整法':
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>使用凑整法：</strong><br>
                        把能凑成整十数的数先结合起来计算<br>
                        逐步计算：<br>
                        ${steps.join('<br>')}
                        = <strong>${answer}</strong>`;

                    case '加法交换律':
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>使用加法交换律：</strong><br>
                        交换加数的位置，方便凑整<br>
                        逐步计算：<br>
                        ${steps.join('<br>')}
                        = <strong>${answer}</strong>`;

                    case '加法结合律':
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>使用加法结合律：</strong><br>
                        把容易计算的数先结合起来<br>
                        逐步计算：<br>
                        ${steps.join('<br>')}
                        = <strong>${answer}</strong>`;

                    default:
                        return `<h3>⚡ 闪电老师讲解：</h3>
                        <strong>逐步计算：</strong><br>
                        ${steps.join('<br>')}
                        = <strong>${answer}</strong>`;
                }
            }'''

# 找到旧的 getExplanation 函数并替换
pattern = r'getExplanation: function\(question, answer, method\) \{[^}]+\n(?:[^}]+\n)*?\s+\}'
matches = list(re.finditer(pattern, content, re.MULTILINE | re.DOTALL))

if matches:
    print(f"找到 {len(matches)} 个匹配")
    for i, match in enumerate(matches):
        print(f"匹配 {i+1}: 位置 {match.start()}-{match.end()}")
        print(f"内容预览: {match.group()[:100]}...")
else:
    print("未找到匹配，尝试其他方法")
    # 尝试另一种匹配方式
    pattern = r'getExplanation: function\(question, answer, method\) \{.*?\n\s+\}'
    matches = list(re.finditer(pattern, content, re.MULTILINE | re.DOTALL))
    if matches:
        print(f"找到 {len(matches)} 个匹配（第二种方式）")
        for i, match in enumerate(matches):
            content = content.replace(match.group(), new_explanation_code, 1)
            print(f"已替换匹配 {i+1}")
            break

# 写回文件
with open('game.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ 文件已更新")
