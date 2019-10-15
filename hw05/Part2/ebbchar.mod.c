#include <linux/build-salt.h>
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x7b7d2c64, "module_layout" },
	{ 0xa321505b, "class_unregister" },
	{ 0xe0ed6bff, "device_destroy" },
	{ 0x4b0bf422, "class_destroy" },
	{ 0x47f007e6, "device_create" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0xb94942b8, "__class_create" },
	{ 0x799b2ee0, "__register_chrdev" },
	{ 0x51a910c0, "arm_copy_to_user" },
	{ 0xefd6cf06, "__aeabi_unwind_cpp_pr0" },
	{ 0xcbd4898c, "fortify_panic" },
	{ 0x5f754e5a, "memset" },
	{ 0x74c09190, "warn_slowpath_fmt" },
	{ 0xd9ce8f0c, "strnlen" },
	{ 0xae353d77, "arm_copy_from_user" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x2e5810c6, "__aeabi_unwind_cpp_pr1" },
	{ 0xc5850110, "printk" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "DF13F5031F1E30D0665301E");
