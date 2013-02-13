#ifndef _SONYELF_H_
#define _SONYELF_H_

typedef struct sonyelf_hdr sonyelf_hdr;
typedef struct sonyelf_sect sonyelf_sect;
typedef struct sonyelf_boot sonyelf_boot;

#define ELF_MAGIC "\x7f\x45\x4c\x46\x01\x01\x01\x61"
#define ELF_MAGIC_SIZE 8

/* These are the section name definitions as found in mkelf.py */
#define RAMDISK_SECTION 0x80000000
#define CMDLINE_SECTION 0x20000000
#define RPM_SECTION     0x01000000

struct sonyelf_hdr
{

    /* This struct data is constructed
     * from the data contained within
     * mkelf.py and suplimented from elf.h
     */

    unsigned char magic[16];

    short type;
    short machine;
    unsigned int version;
    unsigned int entrypoint;
    unsigned int poffset;
    unsigned int voffset;
    unsigned int flags;
    short hsize;
    short phsize;
    short phnum;
    short shsize;
    short shnum;
    short shindex;

};

/* This is how program headers are defined in elf.h */

struct sonyelf_sect
{
    signed int type;
    unsigned int offset;
    unsigned int vaddr;
    unsigned int paddr;
    unsigned int fsize;
    unsigned int msize;
    unsigned int flags;
    unsigned int align;
};

struct sonyelf_boot
{
    unsigned int kernel_paddr;
    unsigned int kernel_offset;
    unsigned int kernel_msize;
    unsigned int ramdisk_paddr;
    unsigned int ramdisk_offset;
    unsigned int ramdisk_msize;
    unsigned int cmdline_offset;
    unsigned int cmdline_msize;
    char cmdline[512];
};

#endif
