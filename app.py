# -*- coding: utf-8 -*-
"""
Streamlit 版实时微任务评分器
"""

import numpy as np
import streamlit as st

# ---------- 参数 ----------
DIMENSIONS = ["目标对齐度A", "影响力B", "紧急性C", "资源消耗D",
              "认知负荷E", "学习成长F", "风险G", "可替代性H"]
WEIGHTS = np.array([0.25,0.25,0.20,0.10,0.05,0.05,0.05,0.05])

# ---------- UI ----------
st.title("实时微任务价值快速评估")
scores = []
for i, dim in enumerate(DIMENSIONS):
    scores.append(
        st.slider(f"{dim} 0=最低 2=最高", 0, 2, 1, key=i)
    )

# ---------- 计算 ----------
total = float(np.dot(WEIGHTS, scores))
if total >= 1.2:
    advise = "✅ 立即执行"
elif total >= 0.8:
    advise = "🕒 放入待办 / 批量执行"
else:
    advise = "🚀 委派或放弃"

st.markdown(f"### 综合得分：{total:.2f}\n\n**决策建议：{advise}**")
