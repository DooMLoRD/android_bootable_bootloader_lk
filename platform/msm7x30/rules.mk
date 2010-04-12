LOCAL_DIR := $(GET_LOCAL_DIR)

ARCH := arm
ARM_CPU := cortex-a8
#arm1136j-s
CPU := generic

MEMBASE := 0x00100000
MEMSIZE := 0x00100000 # 1MB

DEFINES += WITH_CPU_EARLY_INIT=1 WITH_CPU_WARM_BOOT=1

DEFINES += MEMBASE=$(MEMBASE)

INCLUDES += -I$(LOCAL_DIR)/include

DEVS += fbcon
MODULES += dev/fbcon

OBJS += \
	$(LOCAL_DIR)/arch_init.o \
	$(LOCAL_DIR)/platform.o \
	$(LOCAL_DIR)/interrupts.o \
	$(LOCAL_DIR)/gpio.o \
	$(LOCAL_DIR)/acpuclock.o \
	$(LOCAL_DIR)/lcdc.o

LINKER_SCRIPT += $(BUILDDIR)/system-onesegment.ld

include platform/msm_shared/rules.mk

