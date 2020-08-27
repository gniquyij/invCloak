# coding=utf-8
import click
import cv2
import numpy as np


@click.group()
def cli():
    pass


@cli.command(help='Add cloak')
@click.option('-r', '--raw-path', help='Raw image')
@click.option('-c', '--cloak-path', help='Cloak')
@click.option('-d', '--dressed-path', help='Image dressed with cloak')
def add(raw_path, cloak_path, dressed_path):
    raw = cv2.imread(raw_path)
    raw_fft = np.fft.fft2(raw)
    cloak = cv2.imread(cloak_path)
    raw_height, raw_width = raw.shape[0], raw.shape[1]
    cloak_height, cloak_width = cloak.shape[0], cloak.shape[1]
    tmp = np.zeros(raw.shape)
    for x in range(raw_height):
        for y in range(raw_width):
            if x < cloak_height and y < cloak_width:
                tmp[x][y] = cloak[x][y]
    dressed_fft = raw_fft + tmp
    dressed = np.fft.ifft2(dressed_fft)
    dressed = np.real(dressed)
    cv2.imwrite(dressed_path, dressed)


@cli.command(help='Get cloak')
@click.option('-r', '--raw-path', help='Raw image')
@click.option('-d', '--dressed-path', help='Image dressed with cloak')
@click.option('-c', '--cloak-path', help='Cloak')
def get(raw_path, dressed_path, cloak_path):
    raw = cv2.imread(raw_path)
    raw_fft = np.fft.fft2(raw)
    dressed = cv2.imread(dressed_path)
    dressed_fft = np.fft.fft2(dressed)
    cloak = dressed_fft - raw_fft
    cloak = np.real(cloak)
    cv2.imwrite(cloak_path, cloak)


if __name__ == '__main__':
    cli()