/* dev/panel/msm/mipi_r633606_tmd_mdx80.c
 *
 * Copyright (C) 2012 Dominik Marszk
 *
 * Based on mipi_chimei_video_wxga.c
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2; as
 * published by the Free Software Foundation; either version 2
 * of the License, or (at your option) any later version.
 */
 
 
#include <stdint.h>
#include <msm_panel.h>
#include <mipi_dsi.h>
#include <sys/types.h>
#include <err.h>
#include <reg.h>
#include <debug.h>
#include <platform/iomap.h>
#include <mdp4.h>
#include <clock.h>

int mipi_tmd_mdx80_early_config(void *pdata)
{
	uint32_t tmp;
	uint32_t reg = DSI_LANE_CTRL;
	struct msm_panel_info *pinfo = (struct msm_panel_info *)pdata;

	/* Force DSI-clock ON */
	tmp = readl_relaxed(reg);
	tmp |= (1<<28);
	writel_relaxed(tmp, reg);

	mipi_d2l_dsi_init_sequence(pinfo);
}

int mipi_tmd_mdx80_config(void *pdata)
{
	int ret = NO_ERROR;	
	struct lcdc_panel_info *lcdc = NULL;
	struct msm_panel_info *pinfo = (struct msm_panel_info *)pdata;
	unsigned char lane_en = 0x0F; /* 4 Lanes */
	unsigned long low_pwr_stop_mode = 0;
	unsigned char eof_bllp_pwr = 0;
	unsigned char interleav = 0;

	if (pinfo == NULL)
		return ERR_INVALID_ARGS;

	lcdc =  &(pinfo->lcdc);
	if (lcdc == NULL)
		return ERR_INVALID_ARGS;

	ret = mipi_dsi_video_mode_config((pinfo->xres + lcdc->xres_pad),
			(pinfo->yres + lcdc->yres_pad),
			(pinfo->xres),
			(pinfo->yres),
			(lcdc->h_front_porch),
			(lcdc->h_back_porch + lcdc->h_pulse_width),
			(lcdc->v_front_porch),
			(lcdc->v_back_porch + lcdc->v_pulse_width),
			(lcdc->h_pulse_width),
			(lcdc->v_pulse_width),
			pinfo->mipi.dst_format,
			pinfo->mipi.traffic_mode,
			lane_en,
			low_pwr_stop_mode,
			eof_bllp_pwr,
			interleav);

	return ret;
}

int mipi_tmd_mdx80_on()
{
	int ret = NO_ERROR;
	return ret;
}

int mipi_tmd_mdx80_off()
{
	int ret = NO_ERROR;
	return ret;
}

static struct mipi_dsi_phy_ctrl dsi_video_mode_phy_db = {
	/* 720*1280, RGB888, 4 Lane 60 fps video mode */	
	/* regulator */
	.regulator = {0x03, 0x0a, 0x04, 0x00, 0x20},
	/* timing */
	.timing = {0x7b, 0x1b, 0x12, 0x00, 0x40, 0x49, 0x17, 0x1e,
	 0x1e, 0x03, 0x04, 0xa0},	
	/* phy ctrl */
	.ctrl = {0x5f, 0x00, 0x00, 0x10},	
	/* strength */
	.strength = {0xff, 0x00, 0x06, 0x00},	
	/* pll control */
	.pll = {0x00, 0x9e, 0x31, 0xd9, 0x00, 0x50, 0x48, 0x63,
	 0x41, 0x0f, 0x03,
	 0x00, 0x14, 0x03, 0x00, 0x02, 0x00, 0x20, 0x00, 0x01 },
};

/* Initial Sequence */
static char mcap[] = {
	0xB0, 0x00
};

/* Display ON Sequence */
static char cabc_on_off[] = {
	0xBB, 0x0B
};
static char pwm_dimming_control[] = {
	0xBC, 0x00
};
static char pwm_setting_1[] = {
	0xB7, 0x18, 0x00, 0x18, 0x18, 0x0C, 0x14,
	0xAC, 0x14, 0x6C, 0x14, 0x0C, 0x14, 0x00,
	0x10, 0x00
};
static char pwm_setting_2[] = {
	0xB8, 0xF8, 0xDA, 0x6D, 0xFB, 0xFF, 0xFF,
	0xCF, 0x1F, 0x37, 0x5A, 0x87, 0xBE, 0xFF
};
static char cabc_user_param[] = {
	0xBE, 0xFF, 0x0F, 0x00, 0x0C, 0x10, 0x02,
	0x00, 0x5D, 0x00, 0x00, 0x80, 0x32
};
static char exit_sleep[] = {
	0x11
};
static char display_on[] = {
	0x29
};

/* Display OFF Sequence */
static char enter_sleep[] = {
	0x10
};

/* Reading DDB Sequence */
static char read_ddb_start[] = {
	0xA1, 0x00
};

void mipi_tmd_mdx80_init(struct msm_panel_info *pinfo)
{
	if (!pinfo)
		return;

	dprintf(INFO, "mipi-dsi tmd mdx80 driver ver 1.0.\n");
	
	pinfo->xres = 720;
	pinfo->yres = 1280;
	pinfo->type = MIPI_VIDEO_PANEL;
	pinfo->wait_cycle = 0;
	pinfo->bpp = 24;
	pinfo->clk_rate = 431000000;

	pinfo->lcdc.h_back_porch = 45;
	pinfo->lcdc.h_front_porch = 156;
	pinfo->lcdc.h_pulse_width = 3;
	pinfo->lcdc.v_back_porch = 3;
	pinfo->lcdc.v_front_porch = 9;
	pinfo->lcdc.v_pulse_width = 4;
	pinfo->lcdc.hsync_skew = 0;
	pinfo->lvds.channel_mode = LVDS_SINGLE_CHANNEL_MODE;

	pinfo->lcdc.border_clr = 0;		/* black */
	pinfo->lcdc.underflow_clr = 0xff;	/* blue */
	pinfo->lcdc.xres_pad = 0;
	pinfo->lcdc.yres_pad = 0;
	
	/* mipi - general */
	pinfo->mipi.vc = 0; /* virtual channel */
	pinfo->mipi.rgb_swap = DSI_RGB_SWAP_RGB;
	pinfo->mipi.tx_eot_append = true;
	pinfo->mipi.t_clk_post = 0x04;
	pinfo->mipi.t_clk_pre = 0x1b;		/* Calculated */

	pinfo->mipi.dsi_phy_db = &dsi_video_mode_phy_db;

	/* Four lanes are recomended for 1366x768 at 60 frames per second */
	pinfo->mipi.frame_rate = 60; /* 60 frames per second */
	pinfo->mipi.data_lane0 = true;
	pinfo->mipi.data_lane1 = true;
	pinfo->mipi.data_lane2 = true;
	pinfo->mipi.data_lane3 = true;

	pinfo->mipi.mode = DSI_VIDEO_MODE;

	pinfo->mipi.dst_format = DSI_VIDEO_DST_FORMAT_RGB888;

	/* mipi - video mode */
	pinfo->mipi.traffic_mode = DSI_NON_BURST_SYNCH_EVENT;
	pinfo->mipi.pulse_mode_hsa_he = true;

	pinfo->mipi.hfp_power_stop = false;
	pinfo->mipi.hbp_power_stop = false;
	pinfo->mipi.hsa_power_stop = false;
	pinfo->mipi.eof_bllp_power_stop = true;
	pinfo->mipi.bllp_power_stop = true;

	/* mipi - command mode */
	pinfo->mipi.stream = false; /* dma_p */
	pinfo->mipi.mdp_trigger = DSI_CMD_TRIGGER_SW;
	pinfo->mipi.dma_trigger = DSI_CMD_TRIGGER_SW;

	pinfo->mipi.num_of_lanes = 4; /* lanes 0, 1, 2, 3 are enabled */
	pinfo->mipi.panel_cmds = NULL; /* use in mipi_dsi_panel_initialize() */
	pinfo->mipi.num_of_panel_cmds = 0;

	/* Provide config/on/off callbacks */	
	pinfo->on = mipi_tmd_mdx80_on;
	pinfo->off = mipi_tmd_mdx80_off;
	pinfo->config = mipi_tmd_mdx80_config;
	pinfo->early_config = mipi_tmd_mdx80_early_config;
}