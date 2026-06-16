#!/usr/bin/env python3
"""Shared runtime helpers for analysis scripts."""

from __future__ import annotations

import os


def resolve_workers(requested_workers: int, n_tasks: int) -> int:
    if n_tasks <= 0:
        return 1
    if requested_workers > 0:
        return max(1, min(requested_workers, n_tasks))
    auto = os.cpu_count() or 1
    return max(1, min(auto, n_tasks))
