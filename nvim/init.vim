" Basic settings
set clipboard+=unnamedplus
set mouse=i
set ignorecase smartcase
set number relativenumber
set splitbelow splitright
set guicursor=i-ci-ve:ver20,v-c-sm-n-r-cr-o:hor20
set syntax=on
set encoding=utf-8

" Color scheme
" colorscheme ron
hi Comment guifg=#AAAAAA ctermfg=248  gui=ITALIC cterm=NONE
hi LineNr ctermfg=darkgrey
hi StatusLine ctermbg=darkgrey ctermfg=black

" Automate compiling .tex files
autocmd  Bufwritepost *.tex !latexmk -pdf && latexmk -c && rm *.dvi

" Detecting LaTex files
autocmd BufRead,BufNewfile *.tex set filetype=tex 

" Spell Check for LaTex files
" autocmd FileType tex setlocal spell spelllang=eu_us

" Center the screen
autocmd InsertEnter * norm zz

