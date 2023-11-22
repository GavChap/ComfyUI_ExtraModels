"""
List of all VAE configs, with training parts stripped.
"""
vae_conf = {
	### AutoencoderKL ###
	"kl-f4": {
		"type"             : "AutoencoderKL",
		"embed_scale"      : 4,
		"embed_dim"        : 3,
		"z_channels"       : 3,
		"double_z"         : True,
		"resolution"       : 256,
		"in_channels"      : 3,
		"out_ch"           : 3,
		"ch"               : 128, 
		"ch_mult"          : [1,2,4],
		"num_res_blocks"   : 2,
		"attn_resolutions" : [],
	},
	"kl-f8": { # Default SD1.5 VAE
		"type"             : "AutoencoderKL",
		"embed_scale"      : 8,
		"embed_dim"        : 4,
		"z_channels"       : 4,
		"double_z"         : True,
		"resolution"       : 256,
		"in_channels"      : 3,
		"out_ch"           : 3,
		"ch"               : 128, 
		"ch_mult"          : [1,2,4,4],
		"num_res_blocks"   : 2,
		"attn_resolutions" : [],
	},
	"kl-f16": {
		"type"             : "AutoencoderKL",
		"embed_scale"      : 16,
		"embed_dim"        : 16,
		"z_channels"       : 16,
		"double_z"         : True,
		"resolution"       : 256,
		"in_channels"      : 3,
		"out_ch"           : 3,
		"ch"               : 128, 
		"ch_mult"          : [1,1,2,2,4],
		"num_res_blocks"   : 2,
		"attn_resolutions" : [16],
	},
	"kl-f32": {
		"type"             : "AutoencoderKL",
		"embed_scale"      : 32,
		"embed_dim"        : 64,
		"z_channels"       : 64,
		"double_z"         : True,
		"resolution"       : 256,
		"in_channels"      : 3,
		"out_ch"           : 3,
		"ch"               : 128, 
		"ch_mult"          : [1,1,2,2,4,4],
		"num_res_blocks"   : 2,
		"attn_resolutions" : [16,8],
	},
	### VQModel ###
	"vq-f4": {
		"type"             : "VQModel",
		"embed_scale"      : 4,
		"n_embed"          : 8192,
		"embed_dim"        : 3,
		"z_channels"       : 3,
		"double_z"         : False,
		"resolution"       : 256,
		"in_channels"      : 3,
		"out_ch"           : 3,
		"ch"               : 128, 
		"ch_mult"          : [1,2,4],
		"num_res_blocks"   : 2,
		"attn_resolutions" : [],
	},
	"vq-f8": {
		"type"             : "VQModel",
		"embed_scale"      : 8,
		"n_embed"          : 16384,
		"embed_dim"        : 4,
		"z_channels"       : 4,
		"double_z"         : False,
		"resolution"       : 256,
		"in_channels"      : 3,
		"out_ch"           : 3,
		"ch"               : 128, 
		"ch_mult"          : [1,2,2,4],
		"num_res_blocks"   : 2,
		"attn_resolutions" : [32],
	},
	"vq-f16": {
		"type"             : "VQModel",
		"embed_scale"      : 16,
		"n_embed"          : 16384,
		"embed_dim"        : 8,
		"z_channels"       : 8,
		"double_z"         : False,
		"resolution"       : 256,
		"in_channels"      : 3,
		"out_ch"           : 3,
		"ch"               : 128, 
		"ch_mult"          : [1,1,2,2,4],
		"num_res_blocks"   : 2,
		"attn_resolutions" : [16],
	},
	# OpenAI Consistency Decoder
	"Consistency-Decoder": {
		"type" : "ConsistencyDecoder",
		"embed_scale"      : 8,
		"embed_dim"        : 4,
	},
	# SAI Video Decoder
	"SDV-VideoDecoder": {
		"type"             : "AutoencoderKL-VideoDecoder",
		"embed_scale"      : 8,
		"embed_dim"        : 4,
		"z_channels"       : 4,
		"double_z"         : True,
		"resolution"       : 256,
		"in_channels"      : 3,
		"out_ch"           : 3,
		"ch"               : 128, 
		"ch_mult"          : [1,2,4,4],
		"num_res_blocks"   : 2,
		"attn_resolutions" : [],
		"video_kernel_size": [3, 1, 1]
	}
}
