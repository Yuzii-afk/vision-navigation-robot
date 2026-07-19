# ==========================================
# config.py - 项目所有配置文件
# ==========================================

# ---------- GPIO 引脚定义（BCM 编号） ----------
# 左侧电机（板1）
PWMA_LEFT = 12
AIN1_LEFT = 23
AIN2_LEFT = 24

# 右侧电机（板2）
PWMA_RIGHT = 6
AIN1_RIGHT = 27
AIN2_RIGHT = 22

# ---------- PWM 参数 ----------
PWM_FREQ = 1000        # PWM 频率 (Hz)
PWM_MAX_DUTY = 100     # 占空比最大值

# ---------- 电机控制参数 ----------
BASE_SPEED = 30        # 基础速度 (0~100)
MAX_SPEED = 80
KP_TURN = 30          # 转向比例系数 (偏差 → 转向量)

# ---------- 摄像头参数 ----------
CAMERA_WIDTH = 1536
CAMERA_HEIGHT = 864
EXPOSURE_TIME = 20000  # 微秒 ms
AWB_ENABLE = False

# ---------- 视觉处理参数 ----------
RESIZE_SCALE = 4       # 全局搜索时的缩放倍数
ROI_SIZE = 300         # 局部追踪区域边长（像素）
AREA_THRESHOLD = 500   # 轮廓面积最小阈值
MORPH_KERNEL = (5, 5)  # 形态学内核大小

# ---------- 目标跟踪参数 ----------
LOST_THRESHOLD = 5     # 连续丢失多少帧后切回全局搜索
AREA_NEAR = 15000      # Object Too close
AREA_FAR = 2000        # Object Too far

# ---------- PID 参数 ----------
KP = 0.4
KI = 0.0
KD = 0.0

# ---------- 其他 Others ----------
DEBUG_PRINT = True     # 是否打印调试信息