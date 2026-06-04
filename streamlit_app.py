import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from fractions import Fraction

# 유리수를 분수 형태로 표시하는 함수
def format_fraction(num):
    """소수를 분수로 변환하여 표시"""
    frac = Fraction(num).limit_denominator()
    if frac.denominator == 1:
        return str(frac.numerator)
    return f"{frac.numerator}/{frac.denominator}"

# 페이지 설정
st.set_page_config(page_title="이차함수 그래프", layout="wide")

st.title("📊 이차함수 그래프 시뮬레이터")

# 사이드바에 페이지 선택 추가
page = st.sidebar.radio("📑 페이지 선택", ["그래프 눈으로 확인하기", "계수와 그래프의 관계", "계수들의 종합 이해"], label_visibility="collapsed")

# 그래프 페이지
if page == "그래프 눈으로 확인하기":
    st.markdown("### 이차함수식: y = ax² + bx + c")
    st.markdown("슬라이더로 계수를 조정하며 그래프의 변화를 관찰해보세요!")
    
      
    st.markdown("""
    ### 💡 학습 팁
    
    1️⃣ **한 번에 한 계수씩 변경해보세요**
       - "그래프 눈으로 확인하기" 탭에서 한 계수만 움직여보며 그 역할을 이해하세요
    
    2️⃣ **함수 정보 패널을 관찰하세요**
       - 슬라이더를 움직일 때 꼭짓점, 대칭축, y절편이 어떻게 변하는지 확인하세요
    
    3️⃣ **여러 조합을 시도해보세요**
       - 다양한 a, b, c 값의 조합으로 여러 이차함수를 만들어보세요
       - 같은 포물선을 여러 방법으로 표현할 수 있습니다 (완전제곱식, 표준형 등)
    """)
    
    # 사이드바에 슬라이더 배치
    st.sidebar.header("⚙️ 함수 계수 조정")
    a = st.sidebar.slider("a의 값:", -10.0, 10.0, 1.0, 0.5)
    b = st.sidebar.slider("b의 값:", -20.0, 20.0, 0.0, 0.5)
    c = st.sidebar.slider("c의 값:", -20.0, 20.0, 0.0, 0.5)
    
    # 이차함수 계산
    x = np.linspace(-10, 10, 200)
    y = a * x**2 + b * x + c
    
    # 꼭짓점 계산
    if a != 0:
        vertex_x = -b / (2 * a)
        vertex_y = a * vertex_x**2 + b * vertex_x + c
    else:
        vertex_x = None
        vertex_y = None
    
    # 그래프 생성
    fig, ax = plt.subplots(figsize=(10, 7))
    
    # 배경 스타일
    ax.grid(True, alpha=0.3)
    ax.axhline(y=0, color='k', linewidth=0.5)
    ax.axvline(x=0, color='k', linewidth=0.5)
    
    # 함수 그래프
    ax.plot(x, y, 'b-', linewidth=2.5, label=f'y = {format_fraction(a)}x² + {format_fraction(b)}x + {format_fraction(c)}')
    
    # 꼭짓점 표시
    if vertex_x is not None:
        ax.plot(vertex_x, vertex_y, 'ro', markersize=10, label=f'꼭짓점: ({format_fraction(vertex_x)}, {format_fraction(vertex_y)})')
    
    # 축 설정
    ax.set_xlim(-10, 10)
    ax.set_ylim(-50, 50)
    ax.set_xlabel('x', fontsize=12)
    ax.set_ylabel('y', fontsize=12)
    ax.legend(fontsize=11, loc='upper right')
    ax.set_title('이차함수 그래프', fontsize=14, fontweight='bold')
    
    plt.tight_layout()
    
    # 그래프 표시
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.pyplot(fig)
    
    with col2:
        st.markdown("### 📈 함수 정보")
        st.markdown(f"**함수식:** y = {format_fraction(a)}x² + {format_fraction(b)}x + {format_fraction(c)}")
        
        if a != 0:
            st.markdown(f"**꼭짓점:** ({format_fraction(vertex_x)}, {format_fraction(vertex_y)})")
            st.markdown(f"**대칭축:** x = {format_fraction(vertex_x)}")
            st.markdown(f"**y절편:** {format_fraction(c)}")
            
            # 포물선 방향
            if a > 0:
                st.markdown("**포물선:** 아래로 볼록 (최솟값 보유)")
            else:
                st.markdown("**포물선:** 위로 볼록 (최댓값 보유)")
    
    st.markdown("---")
    
    
# 설명 페이지
elif page == "계수와 그래프의 관계":
    st.markdown("### 💡 이차함수 계수의 역할")
    
    st.markdown("""
    ## a (포물선의 방향과 폭)
    
    **포물선의 방향:**
    - **a > 0**: 아래로 볼록한 포물선 (∪ 모양) → 최솟값 보유
    - **a < 0**: 위로 볼록한 포물선 (∩ 모양) → 최댓값 보유
    
    **포물선의 폭:**
    - **|a| 클수록**: 포물선이 좁아짐 (그래프가 가파름)
    - **|a| 작을수록**: 포물선이 넓어짐 (그래프가 완만함)
    
    예시:
    - a = 3: 좁은 아래로 볼록 포물선
    - a = 1/2: 넓은 아래로 볼록 포물선
    - a = -1: 넓은 위로 볼록 포물선
    """)
    
    st.markdown("""
    ## b (포물선의 좌우 이동)
    
    **대칭축의 변화:**
    - 대칭축의 위치: **x = -b/(2a)**
    - b의 값이 변하면 대칭축이 왼쪽(b > 0) 또는 오른쪽(b < 0)으로 이동
    
    **꼭짓점의 변화:**
    - 꼭짓점의 x좌표가 -b/(2a)에 따라 변함
    - 대칭축이 변하면 꼭짓점의 x좌표도 함께 변함
    
    예시:
    - b = 2: 대칭축이 왼쪽으로 이동 (x = -1)
    - b = -4: 대칭축이 오른쪽으로 이동 (x = 2)
    """)
    
    st.markdown("""
    ## c (y절편)
    
    **y축과의 교점:**
    - 그래프가 y축과 만나는 점: **(0, c)**
    - 따라서 c값이 y절편을 결정
    
    **수직 이동:**
    - **c > 0**: 그래프가 위로 이동
    - **c < 0**: 그래프가 아래로 이동
    - 기본 이차함수 y = ax²를 위아래로 c만큼 이동
    
    예시:
    - c = 3: 그래프가 3만큼 위로 이동, y절편은 (0, 3)
    - c = -2: 그래프가 2만큼 아래로 이동, y절편은 (0, -2)
    """)
    
    st.markdown("---")

# 계수들의 종합 이해 페이지
elif page == "계수들의 종합 이해":
    st.markdown("### 🎯 이차함수의 계수들을 종합적으로 이해해봅시다!")
    
    st.markdown("""
    ## 이차함수: y = ax² + bx + c
    
    이차함수는 **세 개의 계수 a, b, c**로 완전히 결정됩니다.
    각 계수가 그래프에 미치는 영향을 정리하면 다음과 같습니다.
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 📊 각 계수의 역할
    
    | 계수 | 역할 | 영향 | 예시 |
    |------|------|------|------|
    | **a** | 포물선의 기본 모양 | • 방향: a>0(아래볼록) / a<0(위볼록)<br>• 폭: \\|a\\|크면 좁음 / \\|a\\|작으면 넓음 | a=2 (좁은 아래볼록)<br>a=-0.5 (넓은 위볼록) |
    | **b** | 대칭축의 위치 | • 대칭축: x = -b/(2a)<br>• 꼭짓점의 x좌표 결정<br>• 포물선 좌우 이동 | b=4 (왼쪽 이동)<br>b=-2 (오른쪽 이동) |
    | **c** | y절편 | • y축 교점: (0, c)<br>• 포물선 위아래 이동<br>• c>0 (위로) / c<0 (아래로) | c=3 (3칸 위)<br>c=-2 (2칸 아래) |
    """)
    
    st.markdown("---")
    
    st.markdown("""
    ### 🔄 계수 변화에 따른 그래프 변화
    
    **a를 변경하면:**
    - 포물선의 **형태가 변함**
    - 꼭짓점의 위치는 변할 수 있음
    - 예: y = x² → y = 2x² (더 좁아짐)
    
    **b를 변경하면:**
    - 포물선이 **좌우로 이동**
    - 대칭축이 이동 (x = -b/2a)
    - 꼭짓점의 x좌표가 변함
    - 예: y = x² → y = x² + 4x (왼쪽으로 이동)
    
    **c를 변경하면:**
    - 포물선이 **위아래로 이동**
    - 꼭짓점의 y좌표가 변함
    - 대칭축과 포물선의 폭은 유지
    - 예: y = x² → y = x² + 3 (위로 3칸 이동)
    """)

    st.markdown("---")
    
    st.markdown("""
    ### 🎓 중요 공식
    
    **꼭짓점의 좌표:**
    $$\\left(-\\frac{b}{2a}, a\\left(-\\frac{b}{2a}\\right)^2 + b\\left(-\\frac{b}{2a}\\right) + c\\right)$$
    
    **또는 간단히:**
    $$x = -\\frac{b}{2a}, \\quad y = c - \\frac{b^2}{4a}$$
    
    **축의 방정식 (대칭축):**
    $$x = -\\frac{b}{2a}$$
    
    **y절편:**
    $$y = c$$
    """)


