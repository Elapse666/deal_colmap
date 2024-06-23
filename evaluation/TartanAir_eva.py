import numpy as np 
from tartanair_tools.evaluation.tartanair_evaluator import TartanAirEvaluator
import os
import glob 
import time
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    # parser.add_argument("--datapath", help="根目录")
    parser.add_argument("--traj_est", type=str, help="path to calibration file")
    parser.add_argument("--traj_gt", type=str, help="path to calibration file")
    args = parser.parse_args()

    traj_est = np.loadtxt(args.traj_est, delimiter=' ')
    traj_ref = np.loadtxt(args.traj_gt, delimiter=' ')[:, [1, 2, 0, 4, 5, 3, 6]]
    

    print(f"traj_est.shape[0] = {traj_est.shape[0]}")

    gt_traj  = traj_ref.astype(np.float64)
    est_traj = traj_est.astype(np.float64)

    from tartanair_tools.evaluation.evaluator_base import ATEEvaluator, RPEEvaluator, KittiEvaluator, transform_trajs, quats2SEs
    ate_eval = ATEEvaluator()
    scale = True
    ate_score, gt_ate_aligned, est_ate_aligned = ate_eval.evaluate(gt_traj, est_traj, scale)
    est_ate_aligned = np.array(est_ate_aligned)
    
    # 打印评估分数
    print(ate_score)

    # print(gt_ate_aligned.shape)
    # 获取名字
    est_str = args.traj_est.split('/')[-1].split('.')[0]   # 截取 traj_est/ETH3D_traj_est.txt ----> ETH3D_traj_est_aligned.txt
    gt_str = args.traj_gt.split('/')[-1].split('.')[0]
    print(est_str)
    print(gt_str)
    np.savetxt('./traj_est_aligned/'+ est_str + '_aligned' +'.txt', est_ate_aligned, fmt='%.3f')
    np.savetxt('./traj_gt_aligned/'+ gt_str + '_aligned' +'.txt', gt_ate_aligned, fmt='%.3f')


